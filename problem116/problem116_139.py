s=list(input())
t=list(input())

count = 0
for i,w in enumerate(s):
    if w != t[i]:
        count += 1

print(count)