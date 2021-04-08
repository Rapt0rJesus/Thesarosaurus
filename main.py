import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def CheckWord(word):
    if word in data:
        return word
    elif word not in data and word.islower():
        word = word.title()
        CheckWord(word)
    elif word not in data and not word.isupper():
        word = word.upper()
        CheckWord(word)
    return word.lower()


def ReturnDefinition(word):
    if word in data:
        return data[word]
    elif word not in data:
        alt = get_close_matches(word, data.keys())
        if len(alt)>0:
            choice = input(f"Could not find this word. Did you mean {alt[0]} ")
            if choice.lower() == 'y':
                return data[alt[0]]
            else:
                print("This word does not exist")
                return " "
        else:
            print("This word does not exist")
            return " "
    return " "

word = input("Enter a word ")
print(*ReturnDefinition(CheckWord(word)), sep = "\n OR \n")