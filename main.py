from stats import count_characters
from stats import word_count
from stats import make_list_of_dicts
from stats import sort_on


def main():
    with open("books/frankenstein.txt") as f:
        text_string = f.read().lower()
    char_count = count_characters(text_string)
    full_word_count = word_count(text_string)
    sorted_char_count = make_list_of_dicts(char_count)
    
    
    
    
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {full_word_count} total words")
    print("--------- Character Count -------")
    #print(char_count)
    #print(char_count)
    #sorted_char_count.sort(reverse=True, key=sort_on)
    for item in sorted_char_count:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")

main()