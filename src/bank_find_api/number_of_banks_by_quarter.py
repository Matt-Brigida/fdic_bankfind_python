import pandas as pd
import requests

base_url = "https://banks.data.fdic.gov/api/"

def number_by_quarter(start, end):
    number = requests.get(base_url + 'summary', params={'filters':'ACTIVE:1', 'limit':6000}).json()['data']
