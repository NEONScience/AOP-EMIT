FROM jupyter/minimal-notebook:python-3.11

# Installing package for libmamba
# switch to root USER to get all admin privileges
USER root
RUN apt-get update && \
    apt-get install -y \
    libfmt-dev \ 
    libtiff5

# switch back to jovyan USER so the person running the container doesn't have admin privileges
# this is the user in the earth analytics python codespaces and the Jupyter default user name
USER jovyan

# Set up conda
RUN conda update conda 
RUN conda config --remove channels conda-forge
RUN conda config --add channels conda-forge

# Create environment
# copies environment.yml from github repo to the Docker image
COPY environment.yml /home/jovyan/ 
# install mamba library into base environment of conda
RUN conda install -n base -c conda-forge mamba
# updating base environment to match the specifications of the environment.yml file
RUN mamba env update -n base -f /home/jovyan/environment.yml

# Activating environment
# modify the .bash_profile file by putting the .sh and conda activate/deactivate code into the .bash profile
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/jovyan/.bash_profile && \
    echo "conda deactivate" >> /home/jovyan/.bash_profile && \
    echo "conda activate base" >> /home/jovyan/.bash_profile
#run the commands we just put into .bash_profile and install the kernel
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate base && python -m ipykernel install --user --name base
# using ~/.bash_profile instead of ~/.bashrc for non-interactive tty (-it) containers
RUN source /home/jovyan/.bash_profile
