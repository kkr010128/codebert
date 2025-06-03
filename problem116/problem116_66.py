s = input()
t = input()
i = 0
for key, val in enumerate(s):
    if (val != t[key]):
        i+=1
print(i)