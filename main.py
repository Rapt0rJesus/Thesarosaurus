import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def ReturnDefinition(word):
    if word not in data:
        alt = get_close_matches(word, data.keys())
        if len(alt)>0:
            choice = input(f"Could not find this word. Did you mean {alt[0]} ")
            if choice.lower() == 'y':
                return data[alt[0]]
        else:
            print("This word does not exist")
            return " "
    return data[word]

word = input("Enter a word ")
print(*ReturnDefinition(word.lower()), sep = "\n OR \n")