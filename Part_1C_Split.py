# Alan Pysnack
# Part 1C: Split Large text file into small text files

def split(line_num):
    lines_per_file = line_num
    smallfile = None

    with open('really_big_file.txt') as bigfile:
        count = 97

        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'x-a{}.txt'.format(chr(count))
                smallfile = open(small_filename, "w")
                count += 1
            smallfile.write(line)
        if smallfile:
            smallfile.close()


user_parameter = input("Type the number of lines you would like your large text file split into, or hit enter to use "
                       "the default value of 750 \n")

if user_parameter == '':
    user_parameter = int(750)

elif user_parameter.isdigit():
    user_parameter = int(user_parameter)

else:
    user_parameter = (int(input("Please enter an integer \n")))

while user_parameter < 450:
    user_parameter = (int(input("Please enter a number greater than 450\n")))

split(user_parameter)
