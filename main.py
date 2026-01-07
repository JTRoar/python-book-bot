from stats import get_book_text

def main():
    tha_book = get_book_text("books/frankenstein.txt")
    print(f"Found {tha_book} total words")

main()