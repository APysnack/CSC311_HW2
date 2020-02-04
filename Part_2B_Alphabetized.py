# Alan Pysnack
# Part 2B: Sort lines in a text file

fname = "TextFile.txt"

new_sentence = []

with open(fname, 'r') as fin:
    line = fin.readlines()

    for item in line:
        sentence = str(item).strip()
        word = sentence.split()
        word.sort()
        new_sentence.append(" ".join(word))

with open('sort_lines.txt', 'w') as fout:
    for item in new_sentence:
        fout.write(item + '\n')