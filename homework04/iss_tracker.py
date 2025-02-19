from typing import List
import requests
from pprint import pprint
import json
import xmltodict

def main():
    response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.content.decode('utf-8')) # used AI to find right format
    json_data = json.dumps(data, indent = 2)
    dict_data = json.loads(json_data)
    state_data = []
    for i in range(len(dict_data["ndm"]["oem"]["body"]["segment"]["data"]["stateVector"])):
        state_data.append(dict_data["ndm"]["oem"]["body"]["segment"]["data"]["stateVector"][i])

    pprint(state_data[1]['EPOCH'])

if __name__ == '__main__':
    main()

