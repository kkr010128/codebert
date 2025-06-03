import fileinput
a_dict = {chr(c): 0 for c in range(97, 123)}
for line in fileinput.input():
    line = line.lower()
    for c in line:
        if c in a_dict:
            a_dict[c] += 1

for k, v in a_dict.items():
    print('{0} : {1}'.format(k, v))

