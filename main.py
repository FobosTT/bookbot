from stats import get_char_count, get_word_count, sort_dict
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main(rel_path):
    true_path = "/home/omarchy/Projects/bootdev/bookbot/" + rel_path
    str = get_book_text(true_path)
    wc = get_word_count(str)
    char_count = get_char_count(str)
    sorted_list = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found in {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


try:
    main(sys.argv[1])
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
