import kaggle

# Specify the dataset URL
dataset_url = 'https://www.kaggle.com/datasets/thedevastator/grocery-product-prices-for-australian-states?fbclid=IwAR1KnP3kiv2h1NrufSHApmnr6IUGjTpDg5UQ0KNXBpb6A7Apu3hT5WXk2HM'

# Download the dataset
kaggle.api.competition_download_files(dataset_url, path='/resources')

# Extract the contents of the ZIP file (optional)
import zipfile
with zipfile.ZipFile('/resources/titanic.zip', 'r') as zip_ref:
    zip_ref.extractall('/resources/')