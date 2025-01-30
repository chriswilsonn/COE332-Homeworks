import csv
import json
from dicttoxml import dicttoxml
import xmltodict
import yaml

data = {}
with open('Meteorite_Landings.json', 'r') as f:
    data = json.load(f)

with open('Meteorite_Landings.csv', 'w') as o:
    csv_dict_writer = csv.DictWriter(o, data['meteorite_landings'][0].keys())
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(data['meteorite_landings'])

# Used AI to figure out how to convert from dict to xml
xml_data = dicttoxml(data, custom_root = 'Meteorite_Landings', attr_type = False)
dataxml = {}
with open('Meteorite_Landings.xml', 'wb') as xml_file:
    xml_file.write(xml_data)

with open('Meteorite_Landings.xml', 'r') as p:
    dataxml = xmltodict.parse(p.read())

print(dataxml['Meteorite_Landings']['meteorite_landings']['item'][0]['name'])

# Used AI to figure out how to convert json to yaml file
with open('Meteorite_Landings.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)

with open('Meteorite_Landings.yaml', 'r') as yaml_file:
    yaml_data = yaml_file.read()

print(yaml_data)

