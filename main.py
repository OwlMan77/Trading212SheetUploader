import os
from dotenv import load_dotenv
from google_sheets import write_to_sheet
from parse import parse_csv, getYear

load_dotenv()

values = parse_csv()
year = getYear()

# Your sheet will need to have three rows, each column is each month of the year: 
    # first row will be deposits
    # second row will be dividends
    # third row will be withdrawals
range = os.getenv('RANGE')

def main(sheet, range):
    write_to_sheet(sheet, range, values)


if __name__ == '__main__':
    main(year, range)