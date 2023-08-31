## import pandas as pd
## import requests
## import time
## 
## base_url = "https://banks.data.fdic.gov/api/"
## 
## ### get all branch locations-------
## ### there are 4801 unique CERTs, so maybe this is all *current* locations
## 
## locations_url = "https://s3-us-gov-west-1.amazonaws.com/cg-2e5c99a6-e282-42bf-9844-35f5430338a5/downloads/locations.csv"
## 
## locations = pd.read_csv(locations_url)
