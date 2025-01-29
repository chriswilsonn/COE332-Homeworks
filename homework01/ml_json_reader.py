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

def check_hemisphere(latitude: float, longitude: float) -> str:
    location = []
    if (latitude > 0):
        location.append('Northern')
    else:
        location.append('Southern')
    if (longitude > 0):
        location.append(f'{location} & Eastern')
    else:
        location.append(f'{location} & Western')
    return(location)

def mass_statistics(list_of_dictionary, key_word):
    total_mass = 0
    masses = []
    for p in range(len(list_of_dictionary)):
        total_mass += float(list_of_dictionary[p][key_word])
        masses.append(float(list_of_dictionary[p][key_word]))
    mass_stats = [total_mass/len(list_of_dictionary), max(masses), min(masses)]

    return mass_stats


with open('Meteorite_Landings.json', 'r') as f:
    ml_data = json.load(f)

print('The Number of Each Type of Meteorite in the Meteorite Landings Dataset is: ')
pprint(meteor_classifier(ml_data['meteorite_landings'], 'recclass'))

hemisphere_list = []
for row in ml_data['meteorite_landings']:
    hemisphere_list.append(check_hemisphere(float(row['reclat']), float(row['reclong'])))

for j in range(len(hemisphere_list)):
    del hemisphere_list[j][0]

updated_hemisphere_list = []
for k in range(len(hemisphere_list)):
    updated_hemisphere_list.append(hemisphere_list[k][0])

grouping_dict = {}
for phrase in updated_hemisphere_list:
    if phrase in grouping_dict:
        grouping_dict[phrase] += 1
    else:
        grouping_dict[phrase] = 1

print('The Number of Times a Meteorite has Landed in each of the following Hemispheres is: ')
print(grouping_dict)


mass_data = mass_statistics(ml_data['meteorite_landings'],'mass (g)')
print('The Average Mass of All Meteorites Recorded is: ')
print(f"{mass_data[0]} g")

print('The Heaviest Meteorite is: ')
print(f"{mass_data[1]} g")

print('The Lightest Meteorite is: ')
print(f"{mass_data[2]} g")
