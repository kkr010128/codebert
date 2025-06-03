input_line = input().rstrip().split(' ')
l = int(input_line[0])
r = int(input_line[1])
d = int(input_line[2])

output = 0

for i in range(l,r+1):
    if i % d == 0:
        output = output + 1
        
print(output)