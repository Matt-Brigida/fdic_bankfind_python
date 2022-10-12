import pandas as pd
import requests

## huntington----
test_cert = 6560
test_rssd = 12311

base_url = "https://banks.data.fdic.gov/api/"

### get all institutions that have ever existed-------

def all_institutions():
    institutions_url = "https://s3-us-gov-west-1.amazonaws.com/cg-2e5c99a6-e282-42bf-9844-35f5430338a5/downloads/institutions.csv"

    institutions = pd.read_csv(institutions_url)
    institutions.index = institutions["FED_RSSD"]
    institutions = institutions.drop(["FED_RSSD"], axis=1)
    institutions["DATEUPDT"] = pd.to_datetime(institutions["DATEUPDT"])
    ## do more handling of types here-------

    return(institutions)

def all_active_institutions() -> pd.DataFrame:
    r"""Get demographic data for all active institutions.
    Arguments: none
    Returns: dataframe with RSSD as index and columns are demographic info.
    Status: working
    """
    active_institutions = requests.get(base_url + 'institutions', params={'filters':'ACTIVE:1', 'limit':6000}).json()['data']

    active_institutions_df = pd.concat([pd.DataFrame(active_institutions[i]) for i in range(len(active_institutions))], 1)
    active_institutions_df = active_institutions_df.drop(["score"], 1)
    active_institutions_df.columns = active_institutions_df.loc["FED_RSSD"]
    active_institutions_df = active_institutions_df.transpose()
    return(active_institutions_df)



### get financials for given CERT------
### https://banks.data.fdic.gov/docs/#/operations/Financials/getFinancials
#### ^ link has a list of variables---is it the full list from the SDI data source?

### lets try pulling everything------
### maybe not possible---stops with an error (Extra data: line 1 column 5 (char 4))
## maybe loop through list of certs
## following works, maybe loop through all RSSDIDs and append to dataframe
### hban = requests.get(base_url + 'financials', params={'filters':'REPDTE:20220630 AND RSSDID:12311', 'limit':10}).json()['data']
## looks like I can get all active banks with an institutions query with ACTIVE:1 filter

def all_financials_for_quarter(quarter, rssds): # quarter string and rssds list

    hban = requests.get(base_url + 'financials', params={'filters':'REPDTE:20220630 AND RSSDID:12311', 'limit':10}).json()['data']
    
    hban_df = pd.concat([pd.DataFrame(hban[i]) for i in range(len(hban))], 1)
    hban_df = hban_df.drop(["score"], 1)
    hban_df.columns = hban_df.loc["RSSDID"]
    hban_df = hban_df.transpose()




### get all branch locations-------
### there are 4801 unique CERTs, so maybe this is all *current* locations

    locations_url = "https://s3-us-gov-west-1.amazonaws.com/cg-2e5c99a6-e282-42bf-9844-35f5430338a5/downloads/locations.csv"

    locations = pd.read_csv(locations_url)
