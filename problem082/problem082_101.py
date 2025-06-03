s = list(input())
t = list(input())
length = len(s)-len(t) + 1
max = 0
for i in range(length):
    count = 0
    for j in range(len(t)):
        if t[j] == s[i+j]:
            count += 1
        if j == len(t)-1 and max < count:
            max = count
print(len(t) - max)