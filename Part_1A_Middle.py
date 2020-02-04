# Alan Pysnack
# Part 1A: Retrieving the middle lines from a text file

fname = "TextFile.txt"
items = list()

try:
    with open(fname) as fin:
        for line in fin:
            items.append(line.strip())

    length = len(items)

    user_parameter = input("Type the number of lines you would like to redact from the top and bottom, or hit the "
                               "enter key if you would like to use the default value of 18 \n")
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
        for item in items[lower:upper]:
            print(item)
except IOError:
    print("Attempt to open file was unsuccessful")