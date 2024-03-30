# Trading212 export to Google Sheet

## Requirements
- Python 3.11.6+ 
- a GCP project with sheets API enabled and a credentials.json file for a service account
- a Google sheet
- a `.csv` export from Trading212

## Description

Since Trading212 is still in its beta stages for its API, I have created a small python project to move all the contents of an annual CSV export from a  Trading212 portfolio to get key statistics for taxes for a Google sheet.

## How to run

1. populate an `.env` file with the following variables
 - `SPREADSHEET_ID` - this is the sheet that you will be writing to
 - `RANGE` - (e.g 'B6:M8') this will be the rows that you will populate:
    - first row will be deposits
    - second row will be dividends
    - third row will be withdrawals

2. `python3 main.py`
