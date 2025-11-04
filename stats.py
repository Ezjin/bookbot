def get_num_words(string):
    words_list = string.split()
    return len(words_list)

def get_num_char(string):
    char_dict = {}
    for c in string:
        c = c.lower()
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_sort_dict(dictionary):
    i = 0
    new_list = []
    for k in dictionary.keys():
        new_list.append({
            "char":k,
            "num": dictionary[k]
        })
        new_list.sort(reverse=True, key=sort_on)
    return new_list