s = [x for x in input()]
t = [y for y in input()]
count = 0
for _ in range(len(s)):
    if s[_] != t[_]:
        count+=1
print(count)