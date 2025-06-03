s = input()
t = input()
numlist = []
for i in range(len(s)-len(t)+1):
    a = s[i:i+len(t)]
    count = 0
    for j in range(len(t)):
        if a[j] != t[j]:
            count += 1
    numlist.append(count)
print(min(numlist))