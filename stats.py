def get_word_count(str):
    words = str.split()
    count = 0
    for word in words:
        count += 1
    return count


def get_char_count(str):
    char_count = {}
    lower_str = str.lower()
    for char in lower_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    list_of_dicts = []
    for entry in dict:
        list_of_dicts.append(
            {"char": entry, "num": dict[entry]}
        )
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
