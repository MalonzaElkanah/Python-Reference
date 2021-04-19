file = open('repeatedLines.txt', 'r')
lines = file.readlines()
print(lines)
k = 1
num = len(lines)
for line in lines:
    i = k
    while i < num:
        if line == '':
            i += 1
        elif line == lines[i]:
            del lines[i]
            num -= 1
        else:
            i += 1
    k += 1
j = 0
new_file = open('non-repeatingLines.txt', 'w')
new_file.flush()
new_file.close()
for line in lines:
    j += 1
    print(str(j)+": "+line)
    new_file = open('non-repeatingLines.txt', 'a')
    new_file.write(line)
