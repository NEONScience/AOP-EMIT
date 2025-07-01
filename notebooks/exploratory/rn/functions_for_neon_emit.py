# For two different data downloads: NEON data & EMIT data
import os
from datetime import datetime

# --- Function to explore multiple data folders ---
def data_download_tracker(base_project_dir, relative_soap_path, folder_names, extension):
    """
    Explores 'SOAP' directory to confirm data downloaded into correct folders and finds files with a specific extension within those folders and their subdirectories.

    Args:
        base_project_dir (str): The absolute path to the root of your project.
        relative_soap_path (str): The path from base_project_dir to the 'SOAP' folder (e.g., "data/SOAP").
        folder_names (list): A list of names of the subfolders within 'SOAP' to explore (e.g., ["EMIT", "NEON"]).
        extension (str): The file extension to search for (".nc", ".shp", ".CHM", ".H5").

    Returns:
        dict: A dictionary where keys are the folder names (e.g., "EMIT", "NEON")
              and values are lists of absolute paths to the found files within that folder.
    """
    soap_directory = os.path.join(base_project_dir, relative_soap_path)
    all_found_files = {} # To store results for each folder
    
    if not os.path.isdir(soap_directory):
        print(f"Error: The 'SOAP' directory does not exist at: {soap_directory}")
        return all_found_files

    print(f"\n--- Starting exploration within the SOAP directory: {soap_directory} ---")

    for folder_name in folder_names:
        current_data_folder = os.path.join(soap_directory, folder_name)
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

# --- Main execution block ---
if __name__ == "__main__":
    # Determine the base directory of the script
    # This assumes your script is in a 'scripts' folder,
    # and 'data' (containing 'SOAP') is parallel to 'scripts'.
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        print("Warning: '__file__' not defined. Assuming current working directory as script_dir.")
        script_dir = os.getcwd() # Or set it to a known path if not running from the script's directory
    
    base_project_dir = os.path.abspath(os.path.join(script_dir, "..")) # Goes up one level from 'scripts'

    relative_path_to_soap = "data/SOAP" # Relative path from base_project_dir
    folder_names = ["EMIT", "NEON"] # Use a list for folder names
    file_extension_to_find = ".nc" # The specific extension you want to find

    # Call the combined function
    print("\n--- Starting Data Download Tracker ---")
    found_nc_files_by_folder = data_download_tracker(
        base_project_dir,
        relative_path_to_soap,
        folder_names,
        file_extension_to_find
    )

    print("\n--- Summary of Found Files ---")
    for folder, files in found_nc_files_by_folder.items():
        if files:
            print(f"In '{folder}': {len(files)} '{file_extension_to_find}' files found.")
            # For brevity, not printing all paths again here, but you could:
            # for f in files:
            #     print(f"  - {f}")
        else:
            print(f"In '{folder}': No '{file_extension_to_find}' files found.")





    

    