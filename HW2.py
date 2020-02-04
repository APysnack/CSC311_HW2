dictionary = {"Abstemious": 'b', "Mississippi": 's', "Gregarious": 'g', "Modification": 'i', "Paramount": 'z'}
sub_string_list = ['stem', 'miss', 'gar', 'fic', 'ram']
i = 0


def location(input_str, in_char):
    count = 0
    location_list = []

    for char in input_str:
        count += 1
        if char == in_char:
            location_list.append(count)
    print(location_list)


def location(input_str, in_char, sub_string):
    count = 0
    location_list = []
    index = 0

    for char in input_str:
        count += 1
        if char == in_char:
            location_list.append(count)
    print(location_list)

    if sub_string in input_str:
        c = sub_string[0]

        for ch in input_str:
            if ch == c:
                if input_str[index:index + len(sub_string)] == sub_string:
                    return index + 1
            index += 1
    return -1

fname = "TextFile.txt"


for item in dictionary:
    word = item
    char = dictionary[item]
    sub = sub_string_list[i]
    i += 1

    print(location(word, char, sub))