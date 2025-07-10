# Function explanations
# Function 1 - The data_tracker function was written as a helpful way 
# to confirm the data files are downloaded in the correct place. 
# We have three different data folders which makes looking through folders 
# manually for specific files cumbersome - using the file extension 
# search helps target specific files..

# Function 2 - We chose to modularize the hvplot.image() function because
# it is lengthy as it includes several parameters. Also, we
# found that almost the exact same parameters (if not the exact
# same) were being used for all plots. This function will make
# it easier to make plots to check our data, such as making sure
# we cropped datasets correctly. We can also use it to easily
# see the surface reflectance for different wavelengths.

# Another step we will take to modularize our workflow is to
# create a for loop to calculate canopy water content (CWC).
# We will create a for loop for this because we have 4 different
# CWC calculations. A for loop will let us easily calculate CWC
# for the two different tiles of interest and the two different datasets.

# Function 1 - data tracker function
# For two different data downloads: NEON data & EMIT data
import os
from datetime import datetime

# --- Function to explore multiple data folders ---
def data_download_tracker(absolute_soap_path, folder_names, extension):
    """
    Explores 'SOAP' directory to confirm data downloaded into correct folders and finds files with a specific extension within those folders and their subdirectories.

    Args:
        absolute_soap_path (str): The absolute path to the root of your project.
        folder_names (list): A list of names of the subfolders within 'SOAP' to explore (e.g., ["EMIT", "NEON"]).
        extension (str): The file extension to search for (".nc", ".shp", ".CHM", ".H5").

    Returns:
        dict: A dictionary where keys are the folder names (e.g., "EMIT", "NEON")
              and values are lists of absolute paths to the found files within that folder.
    """
    all_found_files = {} # To store results for each folder

    if not os.path.isdir(absolute_soap_path):
        print(f"Error: The 'SOAP' directory does not exist at: {soap_directory}")
        return all_found_files

    print(f"\n--- Starting exploration within the SOAP directory: {absolute_soap_path} ---")

    for folder_name in folder_names:
        current_data_folder = os.path.join(absolute_soap_path, folder_name)
        if not os.path.isdir(current_data_folder):
            print(f"Warning: Folder '{folder_name}' does not exist at: {current_data_folder}")
            all_found_files[folder_name] = [] # Record an empty list for this folder
            continue
            
        print(f"\n--- Searching for '{extension}' files in: {current_data_folder} ---")
        
        found_files_in_current_folder = []
        for root, _, files in os.walk(current_data_folder):
            for file in files:
                if file.lower().endswith(extension.lower()):
                    full_path = os.path.join(root, file)
                    found_files_in_current_folder.append(full_path)
                    print(f"Found: {full_path}")

        if found_files_in_current_folder:
            print(f"Found {len(found_files_in_current_folder)} '{extension}' files in '{folder_name}'.")
        else:
            print(f"No '{extension}' files found in '{folder_name}'.")

        all_found_files[folder_name] = found_files_in_current_folder

    return all_found_files

# Function 2 - hvplotter function

def surfrfl_hvplot_image(ds,
                         plottitle,
                         cmap='viridis',
                         clabel='Surface Reflectance (unitless)',
                         geo=True,
                         tiles='ESRI',
                         crs='EPSG:4326',
                         frame_width=720,
                         frame_height=405,
                         transparency=0.7,
                         fontscale=2,
                         xlabel='Longitude',
                         ylabel='Latitude',
                         #kwargs will be a dictionary inside our fxn
                         #this would let a user bypass our fxn and add other .hvplot.image parameters
                         **kwargs):
    """
    Create an interactive surface reflectance plot.
    
    Use hvplot.image() to create an interactive
    plot of one band of surface reflectance provided
    by an xarray.Dataset. The plot has ESRI
    background tiles by default.
    

    Parameters
    -----------
    ds : xarray.Dataset
        Dataset with one band of surface reflectance
    cmap : str, default='viridis'
        Colormap for continuous data
    clabel : str, default='Surface Reflectance (unitless)'
        Colorbar label
    geo : bool, default=True
        Whether the plot is treated as geographic
    tiles : str, default='ESRI'
        The background tiles the geographic data are overlaid on
    crs : str or int EPSG code, default='EPSG:4326'
        Coordinate reference system of the data
    frame_width : int, default=720
        Width of data area of plot
    frame_height : int, default=405
        Height of data area of plot
    transparency : float, default=0.7
        How transparent the plot of the data is
    fontscale : float, default=2
        Scale size of all fonts
    plottitle : str
        Title of the plot
    xlabel : str, default='Longitude'
        x-axis label
    ylabel : str, default='Latitude'
        y-axis label
    **kwargs
        Extra arguments to hvplot.image()


    Returns
    -------
    plot : holoviews.core.overlay.Overlay
        A geographpic surface reflectance plot
        overlaid on basemap tiles.

    Notes
    -----
    Some of the parameter descriptions are based on existing
    descriptions in hvplot documentation[2]_. Further
    information about hvplot.image() can be found on hvplot's
    website[1]_.
    
    References
    ----------
    .. [1] Image—hvPlot 0.11.3 documentation. (n.d.).
    Retrieved June 28, 2025, from https://hvplot.holoviz.org/reference/xarray/image.html
    .. [2] Plotting Options—hvPlot 0.11.3 documentation. (n.d.).
    Retrieved June 28, 2025, from https://hvplot.holoviz.org/ref/plotting_options/index.html
    """
    plot = (
        ds
        .hvplot
        .image(
            #color map
            cmap=cmap,
            #colorbar label
            clabel=clabel,
            #geographic data
            geo=geo,
            #background tiles
            tiles=tiles,
            #map CRS
            crs=crs,
            #plot width & height
            frame_width=frame_width,
            frame_height=frame_height,
            #opacity of surface reflectance data layer
            alpha=transparency,
            #font scale
            fontscale=fontscale,
            #figure title
            title=plottitle,
            #figure x and y labels
            xlabel=xlabel,
            ylabel=ylabel,
            #any desired kwargs
            **kwargs))
    return plot

