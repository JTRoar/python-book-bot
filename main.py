from stats import count_characters
from stats import word_count
from stats import sort_dict


def main():
    with open("books/frankenstein.txt") as f:
        text_string = f.read().lower()
    char_count = count_characters(text_string)
    full_word_count = word_count(text_string)
    sorted_char_count = sort_dict(char_count)
    
    print(full_word_count)
    #print(char_count)
    print(char_count)
    print(sorted_char_count)

main()