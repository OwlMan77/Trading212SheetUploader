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

def getMonthNum(date_string):
    format_with_microseconds = '%Y-%m-%d %H:%M:%S.%f'
    format_without_microseconds = '%Y-%m-%d %H:%M:%S'
    
    try:
        datetime_object = datetime.strptime(date_string, format_with_microseconds)
    except ValueError:
        datetime_object = datetime.strptime(date_string, format_without_microseconds)
    
    return int(datetime_object.month)

def getYear():
   return str(datetime.now().year)

def parse_csv():
    deposits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dividends = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    withdrawals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
                month = getMonthNum(row['Time'])
                if (row['Action'] == 'Deposit'):
                    deposits[month - 1] += float(row['Total'])
                if (row['Action'] == 'Withdrawal'):
                   withdrawals[month - 1] += float(row['Total'])
                if (row['Action'] == 'Dividend (Dividend)'):
                    dividends[month - 1] += float(row['Total'])
    return [deposits, dividends, withdrawals]

