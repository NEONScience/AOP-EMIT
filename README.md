[![DOI](https://zenodo.org/badge/968394746.svg)](https://doi.org/10.5281/zenodo.15300127)

# Seeing the Forest as well as the Trees: Creating a Tutorial to Compare Data Collected From Air and Space


## Project Description:
In this repository, Canopy Water Content (CWC)<sup>1</sup> is calculated with two different data products: Earth Surface Mineral Dust Source Investigation [[EMIT]](https://www.earthdata.nasa.gov/data/catalog/lpcloud-emitl2arfl-001) L2A Surface Reflectance data<sup>2</sup> and Spectrometer Orthorectified Surface Bidirectional Reflectance data from the NSF National Ecological Observatory Network (NEON) program<sup>3</sup>. This repository also evaluates trade-offs between higher resolution data [[NEON]](https://www.neonscience.org/about/faq) vs larger spatial scale data [EMIT].

This repository contains a folder of exploratory notebooks that were completed by Randi Neff (rn), Hannah Rieder (hr), and Bridget Hass (bh) to learn about NEON and EMIT data and CWC. This repository also contains a folder of final notebooks that includes two tutorial notebooks born out of the exploratory notebooks. Others can use these tutorial notebooks to download and process NEON and EMIT reflectance data (01_NEON_EMIT_tutorial_notebook.ipynb) and then calculate and compare CWC using the NEON and EMIT reflectance data (02_NEON_EMIT_tutorial_notebook.ipynb). A tutorial does not currently exist that compares NEON and EMIT reflectance data via CWC. More information about **<a href="#workflow-instructions">Workflow Instructions</a>**, **<a href="#tutorial-notebook-contents">Tutorial Notebook Contents</a>**, and **<a href="#repository-structure">Repository Structure</a>** can be found below.

#### Background:
EMIT measures surface reflectance from the International Space Station (ISS) at 60 meter resolution<sup>2</sup>. NEON operates an Airborne Observation Platform (AOP), which is a set of instruments on a light aircraft that collect high resolution remote sensing data at a low altitude [(see NEON Airborne Remote Sensing webpage)](https://www.neonscience.org/data-collection/airborne-remote-sensing). One of the datasets AOP collects is surface reflectance at 1 meter resolution. 

The area of interest is the NEON Soaproot Saddle Site [(SOAP)](https://www.neonscience.org/field-sites/soap) in the Sierra National Forest in California which contains a mixed conifer forest and was partially burned by the [Creek fire](https://www.fire.ca.gov/incidents/2020/9/4/creek-fire) in 2020. Within the SOAP site, two 1 km by 1 km tiles are focused on: one that was burned by the Creek fire and one that was unburned. Areas that burned and those that remained unburned will potentially show the impact of mortality using high resolution NEON data, which is crucial for understanding post-fire recovery, carbon dynamics and forest hydrology. Canopy Water Content (CWC) is an indicator of tree health and measures the total amount of liquid water in canopy leaves<sup>4</sup>. Measurements of CWC vary based on tree species and can be used to predict mortality. <sup>5</sup> In addition, using EMIT data at a larger scale can show broad patterns of vegetation stress. Ultimately, we will be using the work in this repository to create a tutorial for combining both datasets for a more robust analysis of surface reflectance and forest health.

## Datasets and Requirements:
The following are required. All software or accounts are free. Data can be downloaded via scripts.
1. Earthdata Login account
* Create an Earthdata Login account (if you don't already have one) at [https://urs.earthdata.nasa.gov/users/new](https://urs.earthdata.nasa.gov/users/new)

2. Netrc file
* This file is needed to access NASA Earthdata assets from a scripting environment like Python.
* There are multiple methods to create a .netrc file. The earthaccess package is used to automatically create a netrc file using your Earthdata login credentials if one does not exist. There are detailed instruction available for creating a .netrc file using other methods [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/guides/create_netrc_file.md).

3. A NEON API Token
* Create a Token following [this tutorial](https://www.neonscience.org/resources/learning-hub/tutorials/neon-api-tokens-tutorial)

| Dataset Name  | Short Description | Range, Resolution, and Area | Data Citation |
|---------------|-------------------|-----------------------------|---------------|
| [EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks (EMITL2ARFL)](https://lpdaac.usgs.gov/products/emitl2arflv001/)    | Non-orthorectified surface reflectance derived by screening clouds and correction for atmospheric effects; data is in NetCDF4 files; data can be searched for and downloaded via the earthaccess python library         | August 09, 2022 - ongoing, 60 m spatial resolution, each granule is abt 75 km by 75 km, areas are sunlit regions of interest between 52° N latitude and 52° S latitude            | Green, R. (2022). <i>EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m V001</i> [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2025-06-15 from https://doi.org/10.5067/EMIT/EMITL2ARFL.001                     |
| [NEON - Spectrometer orthorectified surface bidirectional reflectance - mosaic](https://data.neonscience.org/data-products/DP3.30006.002)    | Hyperspectral raster distributed in an open HDF5 format in UTM projection; data can be downloaded via the neonutilities python package<sup>4</sup>         | April 2022 - ongoing; 1 m spatial resolution; each file contains all 426 reflectance bands for a single 1 km by 1 km tile       | NEON (National Ecological Observatory Network). Spectrometer orthorectified surface bidirectional reflectance - mosaic (DP3.30006.002), provisional data. Dataset accessed from https://data.neonscience.org/data-products/DP3.30006.002 on June 16, 2025. |
| NEON - Flight Boundary Dataset Shapefile | NEON AOP flight boundaries in shapefile polygons; these shapefiles can be downloaded manually to the computer or possibly using ArcGIS; these SOAP site flight boundaries will provide the geometries that EMIT data is clipped to | (0-1 unitless, scaled by 10,000) | See the “Flight Boundaries” section on this site: https://www.neonscience.org/data-samples/data/spatial-data-maps |
| [NEON - Ecosystem Structure](https://data.neonscience.org/data-products/DP3.30015.001) | Height of canopy top above bare earth, however in this repository **this dataset was just used for the metadata which includes shapefile boundaries of tiles (.shp, .shx, .prj, .dbf)** | June 2013 - ongoing, 1m spaital resolution, each tile is 1 km by 1 km | NEON (National Ecological Observatory Network). Ecosystem structure (DP3.30015.001), RELEASE-2025. https://doi.org/10.48443/jqqd-1n30. Dataset accessed from https://data.neonscience.org/data-products/DP3.30015.001/RELEASE-2025 on July 6, 2025. |

## Data Release:
1. NEON burned and unburned tile boundary shapefiles: These shapefiles (.shp, .shx, .prj, .dbf) were retrieved from the NEON Ecosystem Structure metadata.
   # **ADD DATA RELEASE INFO HERE**
3. Additional data will be downloaded programmatically within the tutorial notebooks

## <span id="workflow-instructions">Workflow Instructions</span>:

### 1. Set up the Python Environment:
The code for this project will be completed in Jupyter Notebooks in the Python programming language. To run the code, an Interactive Development Environment (IDE) is required to open, use, and edit Jupyter Notebook (.ipynb) files (we recommend Jupyter Notebooks, installed through [Anaconda](https://www.anaconda.com/) or alternatively [Visual Studio Code (VS Code)](https://code.visualstudio.com/)). Additionally, an environment and repository with specific packages and libraries is needed. To create said Python environment (called `lpdaac_vitals` or another name of your choice), there are two options depending on your operating system:

**Option 1 - Windows Operating System:** Create and activate the lpdaac_vitals_environment.yml file. The lpdaac_vitals_environment.yml file was created by exporting the environment used to create the exploratory notebooks in this repository; this environment was created by following option 2 below. Here are the full steps for this option:

1. If not already installed, install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) on your local computer.
2. Download the lpdaac_vitals_environment.yml file to your computer and save it in the desired folder for this project (we'll refer to this as the project-root folder).
3. In the project-root folder, create a new folder called "notebooks" (project-root/notebooks/). In this GitHub repo, navigate to the notebooks/final/ folder and download the 01_NEON_EMIT_tutorial_notebook.ipynb and 02_NEON_EMIT_tutorial_notebook.ipynb files and save them to the project-root/notebooks/ folder on your computer.
4. Open the Command Prompt and use the `cd` command to change directories to the project-root folder.
5. In the Command Prompt, run the following code. Creating the environment may take about 10 minutes.

```
conda env create -n lpdaac_vitals -f lpdaac_vitals_environment.yml
```

```
conda activate lpdaac_vitals
```

**Option 2 - Non-Windows Operating System:** Create lpdaac_vitals environment from scratch:
1. If not already installed, install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) on your local computer.
2. In your file explorer, create a folder to be the project directory for this project (we'll refer to this as the project-root folder).
3. In the project-root folder, create a new folder called "notebooks" (project-root/notebooks/). In this GitHub repo, navigate to the notebooks/final/ folder and download the 01_NEON_EMIT_tutorial_notebook.ipynb and 02_NEON_EMIT_tutorial_notebook.ipynb files and save them to the project-root/notebooks/ folder on your computer.
4. Open your preferred command line interface and change directories to the project-root folder.
5. In the command line interface, run the following code. `conda-forge` installations can take a long time to complete, so we recommend splitting up the installations into two sets, as shown below. The packages can all be installed at once but it may take a prohibitively long time. Either way, we recommend allowing the installations to run over night. See [https://github.com/nasa/VITALS/tree/main/setup](https://github.com/nasa/VITALS/tree/main/setup) for more information. 

```
conda create -n lpdaac_vitals -c conda-forge --yes python=3.10 fiona=1.8.22 gdal earthaccess h5py h5netcdf spectral scikit-image
```

```
conda activate lpdaac_vitals
```

```
conda install -c conda-forge --yes hvplot geoviews rioxarray rasterio geopandas jupyter jupyter_bokeh jupyterlab seaborn dask ray-default
```

### 2. Run the Tutorial Notebooks:

If you'd like to complete the notebooks in VS Code, open the 01_NEON_EMIT_tutorial_notebook.ipynb notebook in VS Code and complete it. Then, open the 02_NEON_EMIT_tutorial_notebook.ipynb in VS Code and complete it.

If you'd like to complete the notebooks in Jupyter Lab or Jupyter Notebooks, run the command `jupyter lab` or `jupyter notebook` in the command line interface once you have the environment activated. In a few seconds, Jupyter Lab or Jupyter Notebooks will open the project-root directory in your web browser. Now, you can open and complete 01_NEON_EMIT_tutorial_notebook.ipynb and then open and complete 02_NEON_EMIT_tutorial_notebook.ipynb.

Please note that the tutorial notebooks include further information:
* Instructions for how to download, save, and access the data for these tutorial notebooks
* Instructions for how to set up your project-root folder for success
* Descriptions about the .py files in the notebooks/final/modules folder in this GitHub repo and instructions for how to download and use the .py files

### 2a. <span id="tutorial-notebook-contents">Tutorial Notebook Contents</span>:
* **The end goal of both tutorial notebooks:** We want canopy water content (CWC) calculations for the burned and unburned tiles of interest at the NEON Soaproot Saddle field site (SOAP). For each tile, we want CWC calculated with EMIT and NEON data. This will allow us to compare CWC between burned and unburned areas AND between lower resolution (EMIT) and higher resolution (NEON) data.

<ol>
  <li>01_NEON_EMIT_tutorial_notebook.ipynb - Identify and download data:</li>
  <ol>
    <li>NEON</li>
    <ol>
      <li>Identify burned and unburned tiles of interest from the NEON AOP data. Identify the UTM coordinates of those tiles (in the tutorial notebook, these coordinates are provided for you).</li>
      <li>Download the NEON Spectrometer orthorectified surface bidirectional reflectance data for the burned and unburned tiles.</li>
      <li>Process the NEON Spectrometer orthorectified surface bidirectional reflectance data for the burned and unburned tiles: convert the hdf5 datasets into xarray.Datasets, apply the scale factor, set bad bands to NaN, and export the xarray.Datasets to NetCDF files.</li>
    </ol>
    <li>EMIT</li>
    <ol>
      <li>Identify EMIT L2A Estimated Surface Reflectance granule(s) that cover the burned and unburned tiles (in the tutorial notebook, this granule is provided for you).</li>
      <li>Download the EMIT L2A Estimated Surface Reflectance granule(s) and open as xarray.Dataset(s).</li>
      <li>Clip/crop the downloaded EMIT L2A Estimated Surface Reflectance granule(s) to the burned and unburned tiles of interest and export the cropped xarray.Datasets to NetCDF files. <em>NOTE: if more than one EMIT granule is needed to cover one of the tiles of interest, those EMIT granules would need to be merged together first and then cropped and exported.</em></li>
    </ol>
  </ol>
  <li>02_NEON_EMIT_tutorial_notebook.ipynb - Calculate canopy water content (CWC) for the following combinations:</li>
  <table>
  <tr>
    <th>           </th>
    <th>Burned Tile</th>
    <th>Unburned Tile</th>
  </tr>
  <tr>
    <td>NEON Reflectance Data</td>
    <td style="text-align:center;">    X    </td>
    <td style="text-align:center;">    X    </td>
  </tr>
  <tr>
    <td>EMIT Reflectance Data</td>
    <td style="text-align: center;"> X </td>
    <td style="text-align:center;"> X </td>
  </tr>
</table>

  <li>02_NEON_EMIT_tutorial_notebook.ipynb - Compare the CWC calculations:</li>
  <ol>
    <li>CWC calculated by lower and higher resolution reflectance data:</li>
    <ol>
      <li>Burned tile CWC between NEON and EMIT reflectance data</li>
      <li>Unburned tile CWC between NEON and EMIT reflectance data</li>
    </ol>
    <li>CWC between burned and unburned areas:</li>
    <ol>
      <li>Burned tile CWC calculated with NEON reflectance data and unburned tile CWC calculated with NEON reflectance data</li>
      <li>Burned tile CWC calculated with EMIT reflectance data and unburned tile CWC calculated with EMIT reflectance data</li>
    </ol>
  </ol>
  <li>Possible extensions:</li>
  <ol>
    <li>Look at different scales:</li>
    <ol>
      <li>How does the comparison between the two data sources change based on the area involved?</li>
      <li>At what point are the comparisons too divergent to be useful? What area is too big for NEON or too small for EMIT?</li>
    </ol>
    <li>Temporal comparisons.</li>
  </ol>
</ol>
      
## <span id="repository-structure">Repository Structure</span>:

```
project-root/
│
├── notebooks/                # Main folder for notebooks
│   ├── exploratory/          # Subfolder for exploratory analysis
│   │   ├── hr/               # Subfolder for Hannah Rieder's notebooks
│   │   │   ├── 01_hr_find_download_data.ipynb
│   │   │   └── 02_hr_visualize_data.ipynb
│   │   ├── rn/               # Subfolder for Randi Neff's notebooks
│   │   │   ├── 01_rn_find_download_data.ipynb
│   │   │   ├── 02_rn_explore_aop_data.ipynb
│   │   │   └── 03_rn_explore_emit_data.ipynb
│   │   ├── bh/               # Subfolder for Bridget Hass's notebooks
│   │   │   ├── 01_bh_find_download_data.ipynb
│   │
│   ├── final/                # Subfolder for finalized notebooks
│   │   ├── modules
│   │   │   ├── .ipynb_checkpoints
│   │   │   ├── __pycache__
│   │   │   ├── __init__
│   │   │   ├── ewt_tools.py
│   │   │   ├── ewt_calc2.py
│   |   |   └── test_functions.py
│   │   ├── 01_NEON_EMIT_tutorial_notebook.ipynb
│   │   └── 02_NEON_EMIT_tutorial_notebook.ipynb
│
├── scripts/                  # Python scripts for processing and analysis
│   ├── preprocess.py
│   └── analysis.py
│
├── data/                     # Data folder (ignored by Git)
│   ├── raw/                  # Raw data (input files)
│   ├── processed/            # Processed data (intermediate files)
│   └── output/               # Final output files
│
├── results/                  # Results (e.g., plots, reports, etc.)
│   ├── figures/
│   └── summary.md
│
├── .gitignore                # Git ignore file
├── README.md                 # Project overview and instructions
└── requirements.txt          # Python dependencies
```

## Sources:

*The list of sources below include some software citations, such as the neonutilities package<sup>6</sup>, as well as references for CWC, NEON, and EMIT information.*

1. Land Processes Distributed Active Archive Center (LP DAAC). Equivalent Water Thickness/Canopy Water Content from Imaging Spectroscopy Data https://nasa.github.io/VITALS/python/03_EMIT_CWC_from_Reflectance.html
2. Green, R. (2022). EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m V001 [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2025-06-15 from https://doi.org/10.5067/EMIT/EMITL2ARFL.001
3. NEON (National Ecological Observatory Network). Spectrometer orthorectified surface directional reflectance - mosaic (DP3.30006.001), RELEASE-2025.Dataset accessed from https://data.neonscience.org/data-products/DP3.30006.001/RELEASE-2025 on June 13, 2025.
4. Asner, G. P., Brodrick, P. G., Anderson, C. B., Vaughn, N., Knapp, D. E., & Martin, R. E. (2015). Progressive forest canopy water loss during the 2012–2015 California drought. PNAS, 113(2). https://doi.org/https://doi.org/10.1073/pnas.152339711
5. Brodrick, P., & Asner, G. (2017). Remotely sensed predictors of conifer tree mortalityduring severe drought. Environmental Research Letters, 12. DOI: 10.1088/1748-9326/aa8f55
6. Claire Lunch, Bridget Hass, Zachary Nickerson and NEON (National Ecological Observatory Network) (2025). neonutilities: Utilities for Working with NEON Data. Python package version 1.1.0. https://doi.org/10.5281/zenodo.15530180


