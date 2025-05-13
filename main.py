import sys
from stats import get_num_words
from stats import string_to_int

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    word_count = get_num_words(book_path)
    character_count = string_to_int(book_path)
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in character_count:
        print(f"{char}: {count}")
    print("============= END ===============")

main()