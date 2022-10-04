import pandas as pd


### get all institutions that have ever existed-------

def all_institutions():
    url = "https://s3-us-gov-west-1.amazonaws.com/cg-2e5c99a6-e282-42bf-9844-35f5430338a5/downloads/institutions.csv"

    institutions = pd.read_csv(url)
    institutions.index = institutions["FED_RSSD"]
    institutions = institutions.drop(["FED_RSSD"], axis=1)
    institutions["DATEUPDT"] = pd.to_datetime(institutions["DATEUPDT"])
    ## do more handling of types here-------

    return(institutions)