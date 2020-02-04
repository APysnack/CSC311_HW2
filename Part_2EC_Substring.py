# Alan Pysnack
# Part 2 EC:  

dictionary = {"Abstemious": 'b', "Mississippi": 's', "Gregarious": 'g', "Modification": 'i',
              "Paramount": 'z', "Precocious": "cio", "UbiQUITous": "quit", "Poppop":"pop",
              "Mundane": "nda", "Biloxi": "cow"}
i = 0


def location(input_str, sub_string):
    count = 0
    location_list = []
    index = 0

    if 2 > len(sub_string) > 0:
        for letter in input_str:
            count += 1
            if letter == sub_string:
                location_list.append(count)
        print(location_list)

    elif len(sub_string) > 1:
        if sub_string in input_str:
            c = sub_string[0]

            for ch in input_str:
                if ch == c:
                    if input_str[index:index + len(sub_string)] == sub_string:
                        location_list.append(index + 1)
                index += 1
        print(location_list)
        return -1

fname = "TextFile.txt"


for item in dictionary:
    word = item.lower()
    sub = dictionary[item].lower()
    i += 1

    location(word, sub)
