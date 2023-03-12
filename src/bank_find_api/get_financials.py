import pandas as pd
import requests
import time

base_url = "https://banks.data.fdic.gov/api/"

### get financials for given RSSD------
### https://banks.data.fdic.gov/docs/#/operations/Financials/getFinancials
#### ^ link has a list of variables---is it the full list from the SDI data source?

def all_financials_for_quarter(quarter, rssds): # quarter string and rssds list
    r"""Get Financial Data for a list of banks over a given quarter.
    Arguments: 
        - quarter: string in YYYYMMDD format
        - rssds: list of integer rssds
    Returns: dataframe 
    Status: Worked for short list.  Need to handle errors.
    """
    ## first get list of columns-------

    temp = requests.get(base_url + 'financials', params={'filters':'REPDTE:'+quarter+' AND RSSDID:'+str('12311'), 'limit':10}).json()['data']
    temp1 = pd.concat([pd.DataFrame(temp[i]) for i in range(len(temp))], 1)
    temp1 = temp1.drop(["score"], 1)
    #temp1.columns = temp1.loc["RSSDID"]
    temp1 = temp1.transpose()
    result_df = pd.DataFrame(columns=list(temp1.columns))  # temp1

    for j in range(len(rssds)):
        time.sleep(10.0)
        try:
	        ll = requests.get(base_url + 'financials', params={'filters':'REPDTE:'+quarter+' AND RSSDID:'+str(rssds[j]), 'limit':10}).json()['data']    
	        df1 = pd.concat([pd.DataFrame(ll[i]) for i in range(len(ll))], 1)
	        df1 = df1.drop(["score"], 1)
	        df1 = df1.transpose()
	        result_df = pd.concat([result_df, df1], ignore_index=True)            
	        #time.sleep(10.0)
	        print("Done with " + str(rssds[j]) + ". Which is " + str(round(100*j/len(rssds), 2)) + "% of the way through.\n", flush=True)
        except:
            pass

    return(result_df)
