from typing import List
import requests
from pprint import pprint
import json
import xmltodict
import time
from datetime import datetime


def year_range(list_of_dicts: List[dict], key_str: str) -> tuple[str, str]:
    '''
     Iterates through a list of dictionaries and finds the first and last values associated with the inputted key. Converts the datetime variables into a Month - Day - Year form a     and returns the date range for which the dataset is applicable.

    Args:
        list_of_dicts (list): a list of dictionaries that have the same set of keys

        key_string (string): a key that appears in each dictionary.

    Returns:
        formatted_date_1 and formatted_date_2: first and last date in the inputted key column formatted in month-day-year format 
    '''

    date_str1 = list_of_dicts[0][key_str]
    date_str2 = list_of_dicts[-1][key_str]
    
    datetime_obj1 = datetime.strptime(date_str1, '%Y-%jT%H:%M:%S.%fZ')
    datetime_obj2 = datetime.strptime(date_str2, '%Y-%jT%H:%M:%S.%fZ')

    formatted_date_1 = datetime_obj1.strftime("%B %d, %Y")
    formatted_date_2 = datetime_obj2.strftime("%B %d, %Y")

    return formatted_date_1, formatted_date_2


def matching_time(list_of_dicts: List[dict], key_str: str) -> dict:
    '''
    Finds the current time using the python time library and converts it to seconds for comaprison purposes. Then iterates through list of dictionaries and finds seconds value for     each date entry. If seconds values match, full epoch is returned. If at the end of the dataset, and no match is found, a message saying no match is found is displayed to the       user.

    Args:
        list_of_dicts (list): a list of dictionaries that have the same set of keys.

        key_string (string): a key that appears in each dictionary.

    Returns:
        list_of_dicts[j]: full epoch (time stamp, state vectors, and velocities) of closest data entry.
    '''
    current_time_s = time.mktime(time.gmtime())
    for j in range(len(list_of_dicts)):
        iteration_time_s = time.mktime(time.strptime(list_of_dicts[j][key_str], '%Y-%jT%H:%M:%S.%fZ'))
        if current_time_s == iteration_time_s:
            return list_of_dicts[j]
        if j==(len(list_of_dicts) - 1):
            print('No Match Found')
        else:
            continue


def main():
    response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.content.decode('utf-8')) # used AI to find right format
    json_data = json.dumps(data, indent = 2)
    dict_data = json.loads(json_data)
    state_data = [] #list of dics
    for i in range(len(dict_data["ndm"]["oem"]["body"]["segment"]["data"]["stateVector"])):
        state_data.append(dict_data["ndm"]["oem"]["body"]["segment"]["data"]["stateVector"][i])
    
    print(f"The data in this dataset is from {year_range(state_data,'EPOCH')[0]} to {year_range(state_data,'EPOCH')[1]}")
    print(matching_time(state_data,'EPOCH'))
    # print(year_range(state_data,'EPOCH'))

if __name__ == '__main__':
    main()

