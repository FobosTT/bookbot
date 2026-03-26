from stats import get_char_count, get_word_count, sort_dict


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main(rel_path):
    true_path = "/Users/fobostt/projects/bookbot/" + rel_path
    str = get_book_text(true_path)
    wc = get_word_count(str)
    char_count = get_char_count(str)
    sorted_list = sort_dict(char_count)
    print("============== BOOKBOT ===============")
    print("Analyzing book found in books/frankenstein.txt...")
    print("-------------- Word Count ----------------")
    print(f"Found {wc} total words")
    print("-------- Character count --------------")
    for char in sorted_list:


main("books/frankenstein.txt")
