# Alan Pysnack
# Part 2C: Output lines with both initials to a text file

fname = "TextFile.txt"
count = 0

word_list = []

# opens file
with open(fname) as fin:

    # reads each line into an array
    my_list = fin.readlines()

    for item in my_list:
        sentence = str(item).strip()
        word = sentence.split()

        for item in word:
            x = item.lower()
            a = x.count('a')
            p = x.count('p')
        if a > 0 and p > 0:
            word_list.append(x)

with open("Words_Containing_Initials.txt", 'w') as fout:
    for item in word_list:
        fout.write(item + '\n')