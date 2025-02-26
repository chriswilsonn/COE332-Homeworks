from typing import List
import requests
from pprint import pprint
import json
import xmltodict
import time
from datetime import datetime
import math
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
    try:
        datetime_obj1 = datetime.strptime(date_str1, '%Y-%jT%H:%M:%S.%fZ')
        datetime_obj2 = datetime.strptime(date_str2, '%Y-%jT%H:%M:%S.%fZ')

        formatted_date_1 = datetime_obj1.strftime("%B %d, %Y")
        formatted_date_2 = datetime_obj2.strftime("%B %d, %Y")

        return formatted_date_1, formatted_date_2
    except ValueError:                                                                                                                                                                     return 'Invalid Date Format'                                                                                                                                               


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
            print('No Match Found for current time.')
        else:
            continue


def speed(list_of_dicts: List[dict]) -> tuple[int, int]:
    '''
    Iterates through a list of dictionaries and finds the xdot, ydot, and zdot velocity components. It then squares each value and sums them together. Next that value is squre roo     ted to find the speed of each datapoint in the dataset. The speed values are then averaged to return the average speed of the ISS from the dataset. If the timestamp matches t      he timestamp when this program is run, the current speed is found using the same process as outlined above.

    Args:
        list_of_dicts (list): a list of dictionaries that have the same set of keys.

    Returns:
        current_speed and average_speed: current speed returns the current speed of the ISS if the timestamps match whereas the average speed returns the average speed across the      dataset
                                                                                                                                                                                       '''
    current_time_s = time.mktime(time.gmtime())
    speed_vals = []
    current_speed = 0
    for k in range(len(list_of_dicts)):
        iteration_time_s = time.mktime(time.strptime(list_of_dicts[k]['EPOCH'], '%Y-%jT%H:%M:%S.%fZ'))
        x_dot = list_of_dicts[k]['X_DOT']['#text']
        y_dot = list_of_dicts[k]['Y_DOT']['#text']
        z_dot = list_of_dicts[k]['Z_DOT']['#text']
        speed_vals.append(math.sqrt(float(x_dot)**2 + float(y_dot)**2 + float(z_dot)**2))
        if current_time_s == iteration_time_s:
            x_dot_1 = list_of_dicts[k]['X_DOT']['#text']
            y_dot_1 = list_of_dicts[k]['Y_DOT']['#text']
            z_dot_1 = list_of_dicts[k]['Z_DOT']['#text']
            current_speed = math.sqrt(float(x_dot_1)**2 + float(y_dot_1)**2 + float(z_dot_1)**2)

    average_speed = sum(speed_vals)/len(speed_vals)

    return average_speed, current_speed

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
    print(f"The average speed of the ISS based on this dataset is {speed(state_data)[0]} km/s and the current speed is {speed(state_data)[1]} km/s. If the current speed is 0, that means no matches were found for the current date." )
    pprint(state_data)


if __name__ == '__main__':
    main()

