def get_word_count(book):
    split = book.split()
    word_count = len(split)
    return word_count

def get_char_count(book):
    char_dict = {}
    lower_book = book.lower()
    char_list = list(lower_book)
    #print(characters)
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_list(dict):
    sorted_list = []
    for key, value in dict.items():
        temp = {"char": key, "num": value}
        sorted_list.append(temp)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    