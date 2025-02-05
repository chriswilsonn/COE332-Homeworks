import csv
from pprint import pprint
from typing import List
import numpy as np
import logging

logging.basicConfig()

def valid_numerical_data(list_of_dicts: List[dict], key_string: str) -> dict:
    '''
    Iterates through a list of dictionaries and finds values associated with the inputted key. Checks to see if the valu    es found are numeric or not. If there is an empty string or non-numeric value, that is considered invalid. 

    Args:
        list_of_dicts (list): a list of dictionaries that have the same set of keys

        key_string (string): a key that appears in each dictionary.

    Returns:
        answer_dict (dictionary): shows the number of valid and invalid rows.

    '''
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

def top_three_years(list_of_dictionaries: List[dict], key: str) -> tuple[list, list]:
    '''
    Iterates through a list of dictionaries and finds values associated with the input key. Manipulates the data to get     it to be in workable format and then finds the three years with the most meteorite landings.

    Args: 
        list_of_dicts (list): a list of dictionaries that have the same set of keys

        key_string (string): a key that appears in each dictionary.
    
    Returns:
        sorted_dates (list) and counts (list): a list with the top 3 years and a list with the number of times a meteori        te landing occured for each of those years.
    '''
    date_str = []
    sorted_dates = []
    counts = []
    for j in range(len(list_of_dictionaries)):
        date_str.append(list_of_dictionaries[j][key][:-19])
    
    unique, occurances = np.unique(date_str, return_counts = True)

    try:
        sorted_indx = np.argsort(occurances)[::-1][:3]
        for b in range(len(sorted_indx)):
            sorted_dates.append(str(unique[sorted_indx[b]]))
            counts.append(int(str(occurances[sorted_indx[b]])))

    except IndexError:
        logging.error('There are not enough points in the dataset to find the top 3 years. ')

    print('The 3 Years with the Most Meteorite Landings are: ')
    print(sorted_dates)

    print('The Number of Times a Meteorite Landing Occured in Each of those Years is: ')
    print(counts)
    
    return sorted_dates, counts


def main():
    
    data = {}
    data['meteorite_landings'] = []

    with open('gh4g-9sfh.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['meteorite_landings'].append(dict(row))

    print(valid_numerical_data(data['meteorite_landings'], 'mass'))

    print(top_three_years(data['meteorite_landings'], 'year'))

if __name__ == '__main__':
    main()



