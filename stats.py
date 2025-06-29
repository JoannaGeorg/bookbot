def get_num_words(content):
    words = content.split()
    word_num = len(words)
    return word_num

def get_char_num(text):
    char_content = text.lower()
    char_num = {}
    for char in char_content:
        if char in char_num:
            char_num[char] += 1
        else:
            char_num[char] = 1
    return char_num

def sort_on(items):
    return items["num"]

def sorted_list(char_dict):
    dict_list = []
    for char in char_dict:
        dict = {"char": char, "num": char_dict[char]}
        dict_list.append(dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
