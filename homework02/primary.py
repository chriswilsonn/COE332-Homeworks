import csv
from pprint import pprint
from typing import List
import numpy as np
import logging

logging.basicConfig()

def valid_numerical_data(list_of_dicts: List[dict], key_string: str) -> dict:
    data_vals = []
    valid_count = 0
    invalid_count = 0
    for i in range(len(list_of_dicts)):
        try:
            value = list_of_dicts[i][key_string]
            if value.strip():
                data_vals.append(int(value))
                valid_count += 1
            else:
                logging.warning(f"Empty string in row {i}.")
                invalid_count += 1
        except ValueError:
            logging.error(f"Non-numeric value in row {i}")
            invalid_count += 1
    
    answer_dict = {
            "Valid Rows": valid_count,
            "Invalid Rows": invalid_count}

    return answer_dict


def main():
    
    data = {}
    data['meteorite_landings'] = []

    with open('gh4g-9sfh.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['meteorite_landings'].append(dict(row))

    print(valid_numerical_data(data['meteorite_landings'], 'mass'))

if __name__ == '__main__':
    main()



