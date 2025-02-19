from typing import List
import requests
from pprint import pprint
import json
import xmltodict
from datetime import datetime


def year_range(list_of_dicts: List[dict], key_str: str) -> tuple[str, str]:
    date_str1 = list_of_dicts[0][key_str]
    date_str2 = list_of_dicts[-1][key_str]
    
    datetime_obj1 = datetime.strptime(date_str1, "%Y-%jT%H:%M:%S.000Z")
    datetime_obj2 = datetime.strptime(date_str2, "%Y-%jT%H:%M:%S.000Z")

    formatted_date_1 = datetime_obj1.strftime("%B %d, %Y")
    formatted_date_2 = datetime_obj2.strftime("%B %d, %Y")

    return formatted_date_1, formatted_date_2

def main():
    response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.content.decode('utf-8')) # used AI to find right format
    json_data = json.dumps(data, indent = 2)
    dict_data = json.loads(json_data)
    state_data = [] #list of dics
    for i in range(len(dict_data["ndm"]["oem"]["body"]["segment"]["data"]["stateVector"])):
        state_data.append(dict_data["ndm"]["oem"]["body"]["segment"]["data"]["stateVector"][i])
    
    print(f"The data in this dataset is from {year_range(state_data,'EPOCH')[0]} to {year_range(state_data,'EPOCH')[1]}")
    # print(year_range(state_data,'EPOCH'))

if __name__ == '__main__':
    main()

