import os
import subprocess
import zipfile

# Set the Kaggle dataset name
dataset_name = "thedevastator/grocery-product-prices-for-australian-states"

# Set the download directory
download_dir = "data/"

# Create the download directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Set the command to download the dataset
download_command = f"kaggle datasets download -d {dataset_name} -p {download_dir}"

# Run the download command
subprocess.call(download_command, shell=True)

# Iterate over all files in the folder
for file_name in os.listdir(download_dir):
    file_path = os.path.join(download_dir, file_name)

    # Check if the file is a ZIP file
    if zipfile.is_zipfile(file_path):
        # Extract the contents of the ZIP file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(download_dir)
        # Delete the ZIP file after extraction
        os.remove(file_path)