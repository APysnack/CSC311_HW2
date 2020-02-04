# Alan Pysnack
# Part 1B: Retrieving the tail and end lines from a text file

fname = "TextFile.txt"
items = list()

try:
    with open(fname) as fin:
        for line in fin:
            items.append(line.strip())

    length = len(items)

    user_parameter = input("Type the number of lines from the head and tail you would like to display (press enter "
                           "for the default value of 18)\n")

    if user_parameter == '':
        user_parameter = int(18)

    elif user_parameter.isdigit():
        user_parameter = int(user_parameter)

    else:
        user_parameter = (int(input("Please enter an integer \n")))

    if length < (2 * user_parameter):
        for item in items:
            print(item)
    else:
        lower = int(user_parameter)
        upper = length - lower
        for item in items[:lower]:
            print(item)
        for item in items[upper:length]:
            print(item)
except IOError:
    print("Attempt to open file was unsuccessful")