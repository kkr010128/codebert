n = int(input())
output = 0
for i in range(n):
    if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:output += i + 1
print(output)