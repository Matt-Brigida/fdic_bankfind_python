import pandas as pd
import requests
import time

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

## cant seem to pull other run dates, so not clear how to get historical data----
# t = requests.get(base_url + 'locations', params={'filters':'RUNDATE:20231013'}).json()['data'] ## RUNDATE:20231020 (can we get historical run dates)
# t_df = pd.concat([pd.DataFrame(t[i]) for i in range(len(t))], 1)

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

