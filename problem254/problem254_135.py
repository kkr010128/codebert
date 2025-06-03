input_line = set([])
input_line.add(int(input()))
input_line.add(int(input()))

for i in range(1,4):
    if i not in input_line:
        print(i)