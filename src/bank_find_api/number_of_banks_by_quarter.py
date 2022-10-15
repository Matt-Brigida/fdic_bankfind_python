import pandas as pd
import requests

base_url = "https://banks.data.fdic.gov/api/"

def number_by_year(year):
    ### looks like only returns yearly data--------
    number = requests.get(base_url + 'summary', params={'filters':'YEAR:[' + str(year) + ' TO ' + str(year) + ']', 'limit':6000, 'fields':'BANKS'}).json()['data']
    number_df = pd.concat([pd.DataFrame(number[i]) for i in range(len(number))], 1)
    number_df = number_df.drop(["score"], 1)

