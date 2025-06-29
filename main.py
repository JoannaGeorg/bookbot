import sys
from stats import get_num_words
from stats import get_char_num
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_char_num(text)
    sorted_num = sorted_list(char_num)
    print(f"Found {num_words} total words")
    for item in sorted_num:
        if item['char'].isalpha() == True:
            print(f"{item['char']}: {item['num']}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])

