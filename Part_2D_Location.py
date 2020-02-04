# Alan Pysnack
# Part 2D: Positions of each character

dictionary = {"Abstemious": 'b', "Mississippi": 's', "Gregarious": 'g', "Modification": 'i', "Paramount": 'z'}

def location(input_str, in_char):
    count = 0
    location_list = []

    for char in input_str:
        count += 1
        if char == in_char:
            location_list.append(count)
    print(location_list)

fname = "TextFile.txt"

for item in dictionary:
    word = item
    char = dictionary[item]
    location(word, char)