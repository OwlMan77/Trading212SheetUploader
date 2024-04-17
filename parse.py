import csv
import os
from datetime import datetime

folder_path = 'put_csv_here!'
first_entry = ''

try:
  with os.scandir(folder_path) as entries:
    first_entry = next(entry for entry in entries if entry.is_file())  # Get first file entry
    if first_entry:
      file_path = os.path.join(folder_path, first_entry.name)
    else:
      print("Folder is empty or inaccessible.")
except FileNotFoundError:
  print(f"Folder not found: {folder_path}")


def get_month(date_string):
    format_with_microseconds = '%Y-%m-%d %H:%M:%S.%f'
    format_without_microseconds = '%Y-%m-%d %H:%M:%S'
    
    try:
        datetime_object = datetime.strptime(date_string, format_with_microseconds)
    except ValueError:
        datetime_object = datetime.strptime(date_string, format_without_microseconds)
    
    return int(datetime_object.month)


def get_date_year(date_string):
    format_with_microseconds = '%Y-%m-%d %H:%M:%S.%f'
    format_without_microseconds = '%Y-%m-%d %H:%M:%S'
    
    try:
        datetime_object = datetime.strptime(date_string, format_with_microseconds)
    except ValueError:
        datetime_object = datetime.strptime(date_string, format_without_microseconds)
    
    return datetime_object.year

def get_current_financial_year_num(month: int, year: int):
    if month >= 4:  # Financial year starts from April
        return year + 1
    else:
        return year

def get_current_financial_year():
    today = datetime.now()
    month = today.month
    year = today.year
    if month >= 4:  # Financial year starts from April
        return f"{year}/{year + 1}"
    else:
        return f"{year - 1}/{year}"

def parse_csv():

    #deposits
    local_deposits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    us_deposits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    #dividends
    local_dividends = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    us_dividends = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # withdrawl
    local_withdrawals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    us_withdrawals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
                raw_month = get_month(row['Time'])
                month = 0
                if raw_month > 3:
                    month = raw_month - 4
                if raw_month < 4: 
                    month = raw_month + 9
                    
                if (row['Action'] == 'Deposit'):
                    if (row['Currency (Total)'] == 'GBP'):
                      local_deposits[month - 1] += float(row['Total'])
                    if (row['Currency (Total)'] == 'USD'):
                      us_deposits[month - 1] += float(row['Total'])
    
                if (row['Action'] == 'Withdrawal'):
                    if (row['Currency (Total)'] == 'GBP'):
                      local_withdrawals[month - 1] += float(row['Total'])
                    if (row['Currency (Total)'] == 'USD'):
                      us_withdrawals[month - 1] += float(row['Total'])

                if (row['Action'] == 'Dividend (Dividend)'):
                    if (row['Currency (Total)'] == 'GBP'):
                      local_dividends[month - 1] += float(row['Total'])
                    if (row['Currency (Total)'] == 'USD'):
                      us_dividends[month - 1] += float(row['Total'])

    return [local_deposits, local_dividends, local_withdrawals, us_deposits, us_dividends, us_withdrawals]

