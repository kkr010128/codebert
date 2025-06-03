N = int(input())
an = x = [int(i) for i in input().split()]

count = 0
for i in range(len(an)):
    if ((i + 1) % 2 == 0):
        continue
    if (an[i] % 2 != 0):
        count = count + 1

print(count)