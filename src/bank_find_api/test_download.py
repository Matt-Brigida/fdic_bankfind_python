


quarter = '20220630'

## huntington----
# test_cert = 6560
# test_rssd = ['12311']

inst = all_active_institutions()

fin_data = all_financials_for_quarter(quarter, list(inst.index[:3]))
