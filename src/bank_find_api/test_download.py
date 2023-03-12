import pandas as pd
import requests
from time import sleep

from get_institutions import all_active_institutions
from get_financials import all_financials_for_quarter

base_url = "https://banks.data.fdic.gov/api/"

quarter = '20220630'

inst = all_active_institutions()

fin_data = all_financials_for_quarter(quarter, list(inst.index[:2]))

#rssds = list(inst.index[:5])
