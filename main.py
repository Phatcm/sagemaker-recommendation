import kaggle

# Download the dataset
kaggle.api.competition_download_files('titanic')

# Specify the destination directory (optional)
kaggle.api.competition_download_files('titanic', path='/path/to/save')

# Extract the contents of the ZIP file (optional)
import zipfile
with zipfile.ZipFile('/path/to/save/titanic.zip', 'r') as zip_ref:
    zip_ref.extractall('/path/to/extract')