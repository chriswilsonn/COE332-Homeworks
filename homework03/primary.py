#!/usr/bin/env python3
import json
import csv
import sys
from pprint import pprint
from typing import List
import numpy as np
import logging
from gcd_algorithm import great_circle_distance

logging.basicConfig()

def valid_numerical_data(list_of_dicts: List[dict], key_string: str) -> dict:
    '''                                                                                          
    Iterates through a list of dictionaries and finds values associated with the inputted key.
    Checks to see if the values found are numeric or not. If there is an empty string or 
    non-numeric value, that is considered invalid.                                                                  
                                                                                                    
    Args:                                                                                                    
        list_of_dicts (list): A list of dictionaries that have the same set of keys.                                                                
        key_string (string): A key that appears in each dictionary.                                                                
                                                                                                    
    Returns:                                                                                                
        answer_dict (dict): A dictionary showing the number of valid and invalid rows.                                      
    '''

    data_vals = []                                                                                                                                                         valid_count = 0                                                                                                                                                        invalid_count = 0                                                                                                                                                      for i in range(len(list_of_dicts)):                                                                                                                                        try:
            key, value = list_of_dicts[i][key_string].split(":")
            print(value)
            if isinstance(value, (int, float)):
                valid_count += 1
            elif value.strip():
                data_vals.append(int(value))                                                                                                                                           valid_count += 1                                                                                                                                                   else:                                                                                                                                                                      logging.warning(f"Empty string in row {i}.")                                                                                                                           invalid_count += 1                                                                                                                                             except ValueError:                                                                                                                                                         logging.error(f"Non-numeric value in row {i}")                                                                                                                         invalid_count += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           answer_dict = {                                                                                                                                                                "Valid Rows": valid_count,                                                                                                                                             "Invalid Rows": invalid_count}                                                                                                                                                                                                                                                                                                        return answer_dict   

def top_three_years(list_of_dictionaries: List[dict], key: str) -> tuple[list, list]:
    '''
    Iterates through a list of dictionaries and finds values associated with the input key. Manipulates the data to get it to be in workable format and then finds the three years     with the most meteorite landings.

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
        if date_str[j] == '':
            logging.error('Date found is in incorrect format. It must look like this: 1880-01-01T00:00:00.000')


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


def landing_distance(list_dicts: List[dict], meteor1_name: str, meteor2_name: str) -> float:
    '''
    Iterates through a list of dictionaries and finds the latitude and longitude values associated with the two inputted meteorite names. Formats the latitude and longitude values    so that they can be fead as floats into the great circle distance function imported into this file. This function then returns the distance between the two meteorites. 

    Args:

        list_of_dicts (list): a list of dictionaries that have the same set of keys

        meteor1_name (string): name of one of the meteors present in the dataset

        meteor2_name (string): name of another metoer present in the dataset

    Returns:
        distance (float): the distance the two meteorites are away from each other calculated using the great circle distance algorithm

    '''
    location_data = []
    for v in range(len(list_dicts)):
        if list_dicts[v]['name'] == meteor1_name:
            location_data.append(list_dicts[v]['geolocation'])
        elif list_dicts[v]['name'] == meteor2_name:
            location_data.append(list_dicts[v]['geolocation'])
        else:
            continue

    try:
        located_data = [location_data[0].strip('()'), location_data[1].strip('()')]
        located_data_list = []
        for k in range(len(located_data)):
            located_data_list.append(located_data[k].split(', ')) 
        

    except IndexError:
        logging.error('Invalid meteor name entered')

    distance = great_circle_distance(float(located_data_list[0][0]),float(located_data_list[0][1]),float(located_data_list[1][0]),float(located_data_list[1][1]))

    return distance



def main():
    
    data = {}
    data['meteorite_landings'] = []

    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['meteorite_landings'].append(dict(row))

    print(valid_numerical_data(data['meteorite_landings'], 'fall:"Fell"')) 
    print(top_three_years(data['meteorite_landings'], 'year'))
    
    print(f" The distance the two meteorites are from each other in km is {landing_distance(data['meteorite_landings'], 'Aire-sur-la-Lys', 'Al Zarnkh')}")


if __name__ == '__main__':
    main()



