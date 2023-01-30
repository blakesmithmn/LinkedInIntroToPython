# TURNING CSV INTO JSON

import csv # read the CSV data
import json # JSON module utility!
from pprint import pprint

# REMEMBER THIS IS A DICTIONARY
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #creating a variable that is the json of the einstein dictionary
back_to_dict = json.loads(einstein_json) # creating a variable that convers the JSON back to dictionary
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f: #bringing in CSV data in 'r' read mode
    reader = csv.DictReader(f) # creating a dictionary using the data
    laureates = list(reader) # creating an array of the dictionaries 


with open("laureates.json", "w") as f: # opening the existing JSON file in 'w' write mode
    json.dump(laureates, f, indent=2) # dump all of our information into the file ... from list laureates into file 'f' and level of indentation which is 2
