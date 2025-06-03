input_line = list(map(int, input().split(' ')))
result = False
for x in list(set(input_line)):
    if input_line.count(x) == 2:
        result = True
if result:
    print('Yes')
else:
    print('No')