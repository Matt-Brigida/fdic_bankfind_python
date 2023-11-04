## BankFind API 

Wrapper around the FDIC Data API:  https://banks.data.fdic.gov/docs/

## Goal of the Package

The FDIC used to provide a zip file of CSVs that contained all call report submissions for each quarter.  This was incredibly useful---you could easily download data for all banks.  However in Q3 2022 the FDIC stopped posting these files. 

The goal of this package is to replicate the earlier service.  That is, to download call repot data for all banks for any given quarter.  If that proves problematic, then the goal of this package is to be able to pull as much data as possible from the FDIC's Bankfind API.  

##  A More Targeted Package

If you want a package that offers targeted queries (the way the API is intended to be used) I would recommend: https://github.com/dpguthrie/bankfind 

# Install

The package is not on PyPi (which now requires a 2FA authenticator app which I haven't gotten around to installing).  To install then package you can clone the repo and `python -m build` in the directory with `pyproject.toml`.  Install the .whl with `pip install` and the you can `from bulkcr import get_institutions` for example.
