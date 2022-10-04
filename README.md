## BankFind API 

Wrapper around the FDIC Data API:  https://banks.data.fdic.gov/docs/

## Goal of the Package

The FDIC used to provide a zip file of CSVs that contained all call report submissions for each quarter.  This was incredibly useful---you could easily download data for all banks.  However in Q3 2022 the FDIC stopped posting these files. 

The goal of this package is to replicate the earlier service.  That is, to download call repot data for all banks for any given quarter.  If that proves problematic, then the goal of this package is to be able to pull as much data as possible from the FDIC's Bankfind API.  

##  A More Targeted Package

If you want a package that offers targeted queries (the way the API is intended to be used) I would recommend: https://github.com/dpguthrie/bankfind 
