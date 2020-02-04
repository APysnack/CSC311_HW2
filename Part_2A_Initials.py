# Alan Pysnack
# Part 2A: # Occurrences of initials and first line with both initials

fname = "TextFile.txt"
count = 0

with open(fname) as fin:

    my_list = fin.readlines()

    line_with_both = -1
    line_num = 0

    for line in my_list:
        line_num += 1
        x = line.lower()
        count += x.count('a')
        count += x.count('p')
        if x.count('a') > 0 and x.count('p') > 0 and line_with_both < 0:
            line_with_both = line_num

print(count)
print(line_with_both)