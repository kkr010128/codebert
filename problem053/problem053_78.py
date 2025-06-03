count = int(input())
line = input().split()
line.reverse()
for i in range(count):
    print(line[i], end = "")
    if i != count-1:
        print(" ", end = "")
print()
