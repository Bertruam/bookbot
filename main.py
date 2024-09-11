path_to_file = "books/frankenstein.txt"
text = open(path_to_file).read()

def sorting(dictio):
    sorted_dict = dict(sorted(dictio.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict   

def count_character():
    low_string = text.lower()
    counter = {}

    for char in range(0,len(low_string)):
        if low_string[char] in counter and low_string[char].isalpha():
            counter[low_string[char]] += 1
        elif low_string[char].isalpha():
            counter[low_string[char]] = 1

    
    sort_dict =sorting(counter)
    key_list = list(sort_dict.keys())
    value_list = list(sort_dict.values())

    for entry in range(0,len(counter)):
        print(f"The {key_list[entry]} character was found {value_list[entry]} times.")

def word_count():
    words = text.split()
    print(f"{len(words)} words found in source file\n")

def main():
    print(f"--- Begining report of {path_to_file} --- ")
    word_count()
    count_character()
    print("--- Report Concluded ---")

main()