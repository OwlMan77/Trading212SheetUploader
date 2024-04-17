import os
from dotenv import load_dotenv
from google_sheets import write_to_sheet
from parse import parse_csv
import operator

load_dotenv()

values = parse_csv()
year = '2023/2024'

# Your sheet will need to have three rows, each column is each month of the year: 
    # first row will be domestic deposits
    # second row will be domestic dividends
    # third row will be domestic withdrawals
    # fourth row will be us deposits
    # fifth row will be us dividends
    # sixth row will be us withdrawals

local_range = os.getenv('LOCAL_RANGE')
us_range = os.getenv('US_RANGE')

get_local_values = operator.itemgetter(0, 1, 2)
get_us_values = operator.itemgetter(3, 4, 5)

print(local_range, us_range)

def main(sheet, local_range, us_range):
    local_values = get_local_values(values)
    us_values= get_us_values(values)
    
    write_to_sheet(sheet, local_range, local_values)
    write_to_sheet(sheet, us_range, us_values)


if __name__ == '__main__':
    main(year, local_range, us_range)