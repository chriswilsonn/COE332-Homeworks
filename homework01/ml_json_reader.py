import json 
from pprint import pprint

def meteor_classifier(list_of_dicts, key_string):
    classifications = []
    for i in range(len(list_of_dicts)):
        classifications.append(list_of_dicts[i][key_string])
    
    word_count_dict = {}

    for word in classifications:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    return(word_count_dict)


with open('Meteorite_Landings.json', 'r') as f:
    ml_data = json.load(f)

print('The Number of Each Type of Meteorite in the Meteorite Landings Dataset is: ')
pprint(meteor_classifier(ml_data['meteorite_landings'], 'recclass'))


