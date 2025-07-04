[![DOI](https://zenodo.org/badge/968394746.svg)](https://doi.org/10.5281/zenodo.15300127)

# Comparing Canopy Water Content using Hyperspectral Data

## Project Description:
In this repository, Canopy Water Content (CWC)<sup>1</sup> is calculated with two different data products: Earth Surface Mineral Dust Source Investigation [[EMIT]](https://earth.jpl.nasa.gov/emit/data/data-products/)<sup>2</sup> L2A Surface Reflectance data and Spectrometer Orthorectified Surface Bidirectional Reflectance data from the NSF National Ecological Observatory Network program<sup>3</sup>. This repository also evaluates trade-offs between higher resolution data [[NEON]](https://www.neonscience.org/about/faq) vs larger spatial scale data [EMIT].

#### Background:
EMIT measures surface reflectance from the International Space Station (ISS) at 60 meter resolution [(Green, 2023)](https://lpdaac.usgs.gov/products/emitl2bminv001/). NEON operates an Airborne Observation Platform (AOP), which is a set of instruments on a light aircraft that collect high resolution remote sensing data at a low altitude [(see NEON Airborne Remote Sensing webpage)](https://www.neonscience.org/data-collection/airborne-remote-sensing). One of the datasets AOP collects is surface reflectance at 1 meter resolution. 

The area of interest is the NEON Soaproot Saddle Site [(SOAP)](https://www.neonscience.org/field-sites/soap) in the Sierra National Forest in California which contains a mixed conifer forest and was the site of two wildfires - the [Creek fire](https://www.fire.ca.gov/incidents/2020/9/4/creek-fire) in 2020 and the [Blue fire](https://www.fire.ca.gov/incidents/2021/6/30/blue-fire/) in 2021. Areas that burned and those that remained unburned will potentially show the impact of mortality using high resolution NEON data, which is crucial for understanding post-fire recovery, carbon dynamics and forest hydrology. Canopy Water Content [CWC] is an indicator of tree health and measures the total amount of liquid water in canopy leaves. <sup>5</sup> Measurements of CWC vary based on tree species and can be used to predict mortality. <sup>6</sup> In addition, using EMIT data at a larger scale can show broad patterns of vegetation stress. Ultimately, we will be using the work in this repository to create a tutorial for combining both datasets for a more robust analysis of surface reflectance and forest health.

## Datasets and Requirements:
The following are required. All software or accounts are free. Data can be downloaded via scripts.
1. Earthdata Login account
Create an Earthdata Login account (if you don't already have one) at [https://urs.earthdata.nasa.gov/users/new](https://urs.earthdata.nasa.gov/users/new)

2. Netrc file
* This file is needed to access NASA Earthdata assets from a scripting environment like Python.
* There are multiple methods to create a .netrc file. The earthaccess package is used to automatically create a netrc file using your Earthdata login credentials if one does not exist. There are detailed instruction available for creating a .netrc file using other methods [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/guides/create_netrc_file.md).

| Dataset Name                                                                                                                                            | Short Description                                                                                                                                                                                                                                                                         | Range, Resolution, and Area                                                                       | Data Citation                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks (EMITL2ARFL)](https://lpdaac.usgs.gov/products/emitl2arflv001/)                                                             | Non-orthorectified surface reflectance derived by screening clouds and correction for atmospheric effects; data is in NetCDF4 files; data can be searched for and downloaded via the earthaccess python library                                                                                                                                              | August 09, 2022 - ongoing, 60 m spatial resolution, each granule is abt 75 km by 75 km, areas are sunlit regions of interest between 52° N latitude and 52° S latitude            | Green, R. (2022). <i>EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m V001</i> [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2025-06-15 from https://doi.org/10.5067/EMIT/EMITL2ARFL.001                                          |
| [NEON - Site management and event reporting](https://data.neonscience.org/data-products/DP1.10111.001) | Records of land management activities, disturbances, and other notable ecological events for all NEON aquatic and terrestrial sites; data can be downloaded via the neonutilities python package<sup>4</sup>      ; these data will be used to understand details about the fires that happened at the SOAP site and any other events that could affect the CWC calculations | July 2012 - ongoing; data has date, location, type, and numerical extent of event if possible | NEON (National Ecological Observatory Network). Site management and event reporting (DP1.10111.001), RELEASE-2025. https://doi.org/10.48443/af3c-5w64. Dataset accessed from https://data.neonscience.org/data-products/DP1.10111.001/RELEASE-2025 on May 2, 2025.                                                                                                                                                             |
| [NEON - Spectrometer orthorectified surface bidirectional reflectance - mosaic](https://data.neonscience.org/data-products/DP3.30006.002)    | Hyperspectral raster distributed in an open HDF5 format in UTM projection; data can be downloaded via the neonutilities python package<sup>4</sup>                                       | April 2022 - ongoing; 1 m spatial resolution; each file contains all 426 reflectance bands for a single 1 km by 1 km tile       | NEON (National Ecological Observatory Network). Spectrometer orthorectified surface bidirectional reflectance - mosaic (DP3.30006.002), provisional data. Dataset accessed from https://data.neonscience.org/data-products/DP3.30006.002 on June 16, 2025. |
| NEON - Flight Boundary Dataset Shapefile | NEON AOP flight boundaries in shapefile polygons; these shapefiles can be downloaded manually to the computer or possibly using ArcGIS; these SOAP site flight boundaries will provide the geometries that EMIT data is clipped to | (0-1 unitless, scaled by 10,000) | See the “Flight Boundaries” section on this site: https://www.neonscience.org/data-samples/data/spatial-data-maps 
| Fire Perimeter Boundary from [CalFire](https://www.arcgis.com/home/item.html?id=692135b4e6ff47c8adae066ff477f4f1#overview) | Fire perimeters for fires greater than 50 acres in California between 2019 and 2023; these data will help determine which parts of SOAP site were burned and unburned for CWC comparison | resolution unknown | California Fire Perimeters last 5 years View—Overview. (n.d.). Retrieved May 2, 2025, from https://www.arcgis.com/home/item.html?id=692135b4e6ff47c8adae066ff477f4f1#overview|

*We do not have Data Releases ready yet, they will be added later. We anticipate having a data release for the NEON spectrometer data and a data release for the EMITL2A reflectance data. For each dataset, we anticipate having a data release of a clipped version of each dataset clipped to our NEON field site of interest.*

## Instructions to Set up the Python Environment:
The code for this project will be completed in Jupyter Notebooks in the Python programming language. To run the code, an Interactive Development Environment (IDE) is required to open, use, and edit Jupyter Notebook (.ipynb) files (we recommend Jupyter Notebooks, installed through [Anaconda](https://www.anaconda.com/) or alternatively [Visual Studio Code](https://code.visualstudio.com/)). Additionally, an environment and repository with specific packages and libraries is needed. To create said Python environment (called `lpdaac_vitals` or another name of your choice), there are two options:

**Option 1:** Use lpdaac_vitals_environment.yml file (recommended): The lpdaac_vitals_environment.yml file was created by exporting the environment used to create the notebooks in this repository; this environment was created by following option 2 below. Option 1 may take about ten minutes to create the environment. Ensure [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) are installed, and then use these commands depending on whether you have conda or mamba installed:

Mamba code:
```
mamba env create -n lpdaac_vitals -f lpdaac_vitals_environment.yml
```

```
mamba activate lpdaac_vitals
```

Conda code:
```
conda env create -n lpdaac_vitals -f lpdaac_vitals_environment.yml
```

```
conda activate lpdaac_vitals
```

**Option 2:** Create lpdaac_vitals environment from scratch: Ensure [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) is installed and then use these commands:

```
mamba create -n lpdaac_vitals -c conda-forge --yes python=3.10 fiona=1.8.22 gdal earthaccess h5py h5netcdf spectral scikit-image
```

```
mamba activate lpdaac_vitals
```

```
mamba install -c conda-forge --yes hvplot geoviews rioxarray rasterio geopandas jupyter jupyter_bokeh jupyterlab seaborn dask ray-default
```

See https://github.com/nasa/VITALS/tree/main/setup for more information. 

Notes: `conda-forge` installations can take a long time to complete, so we recommend splitting up the installations into two sets, as shown above. The packages can all be installed at once but it may take a prohibitively long time. Either way, we recommend allowing the installations to run over night.

## Workflow Instructions
* **The end goal of these steps:** We want canopy water content (CWC) calculations for the burned and unburned tiles of interest at the NEON Soaproot Saddle field site (SOAP). For each tile, we want CWC calculated with EMIT and NEON data. This will allow us to compare CWC between burned and unburned areas AND between lower resolution (EMIT) and higher resolution (NEON) data to develop a tutorial for others interested in these two data sources.

### Steps:

<ol>
  <li>Identify and download data:</li>
  <ol>
    <li>NEON</li>
    <ol>
      <li>Identify burned and unburned tiles of interest from the NEON AOP data. Identify the latitude and longitude of those tiles.</li>
      <li>Download the NEON Spectrometer orthorectified surface bidirectional reflectance data for the burned and unburned tiles.</li>
    </ol>
    <li>EMIT</li>
    <ol>
      <li>Identify EMIT L2A Estimated Surface Reflectance granule(s) that cover the burned and unburned tiles.</li>
      <li>Download the EMIT L2A Estimated Surface Reflectance granule(s)</li>
      <li>Clip/crop the downloaded EMIT L2A Estimated Surface Reflectance granule(s) to the burned and unburned tiles of interest. <em>NOTE: if more than one EMIT granule is needed to cover one of the tiles of interest, those EMIT granules would need to be merged together first.</em></li>
    </ol>
  </ol>
  <li>Calculate canopy water content (CWC) for the following combinations:</li>
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

  <li>Compare the CWC calculations:</li>
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
  <li>Extensions if we have time:</li>
  <ol>
    <li>Look at different scales:</li>
    <ol>
      <li>How does the comparison between the two data sources change based on the area involved?</li>
      <li>At what point are the comparisons too divergent to be useful? What area is too big for NEON or too small for EMIT?</li>
    </ol>
    <li>Temporal comparisons.</li>
  </ol>
  <li>Develop Tutorial.</li>
</ol>
      
## Repository Structure:

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
│   │   ├── 01_find_and_download_collocated_data.ipynb
│   │   ├── 02_aop_endmember_extraction.ipynb
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

1. Land Processes Distributed Active Archive Center (LP DAAC). Equivalent Water Thickness/Canopy Water Content from Imaging Spectroscopy Data https://nasa.github.io/VITALS/python/03_EMIT_CWC_from_Reflectance.html
2. Green, R. (2022). EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m V001 [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2025-06-15 from https://doi.org/10.5067/EMIT/EMITL2ARFL.001
3. NEON (National Ecological Observatory Network). Spectrometer orthorectified surface directional reflectance - mosaic (DP3.30006.001), RELEASE-2025.Dataset accessed from https://data.neonscience.org/data-products/DP3.30006.001/RELEASE-2025 on June 13, 2025.
4. Claire Lunch, Bridget Hass, Zachary Nickerson and NEON (National Ecological Observatory Network) (2025). neonutilities: Utilities for Working with NEON Data. Python package version 1.1.0. https://doi.org/10.5281/zenodo.15530180
5. Asner, G. P., Brodrick, P. G., Anderson, C. B., Vaughn, N., Knapp, D. E., & Martin, R. E. (2015). Progressive forest canopy water loss during the 2012–2015 California drought. PNAS, 113(2). https://doi.org/https://doi.org/10.1073/pnas.152339711
6. Brodrick, P., & Asner, G. (2017). Remotely sensed predictors of conifer tree mortalityduring severe drought. Environmental Research Letters, 12. DOI: 10.1088/1748-9326/aa8f55

*The list of sources above includes some software citations, such as the neonutilities package. We will add more software, packages, and libraries to the sources list as we complete our work this summer.*


