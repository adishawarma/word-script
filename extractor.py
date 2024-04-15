import json


def extract_n_letter_words(json_file_path: str, n: int) -> None:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    n_letter_words = [word for word in data if len(word) == n]
    
    if n_letter_words:
        for word in n_letter_words:
            print(f'"{word}",')
    else:
        print(f"There are no words present in the JSON file of the specified length of {n} letters.")

    
json_file_path = 'words_dictionary.json'
n = int(input("Please enter the number of letters you require in a word: "))

extract_n_letter_words(json_file_path, n)
