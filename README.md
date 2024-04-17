# Trading212 export to Google Sheet

## Requirements
- Python 3.11.6+ 
- a GCP project with sheets API enabled and a credentials.json file for a service account
- a Google sheet that the service account has access to
- a `.csv` export from Trading212

## Description

Since Trading212 is still in its beta stages for its API, I have created a small python project to move all the contents of an annual CSV export from a  Trading212 portfolio to get key statistics for taxes for a Google sheet.

## How to run

1. populate an `.env` file with the following variables
 - `SPREADSHEET_ID` - this is the sheet that you will be writing to
 - `LOCAL_RANGE` - (e.g 'B6:M8') this will be the rows that you will populate with UK based invesments:
    - first row will be domestic deposits
    - second row will be domestic dividends
    - third row will be domestic withdrawals
  - `US_RANGE` - (e.g 'B6:M8') this will be the rows that you will populate with UK based invesments:  
    - fourth row will be US deposits
    - fifth row will be US dividends
    - sixth row will be US withdrawals


2. `python3 main.py`
