import os
import subprocess

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