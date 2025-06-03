s = str(input())
t = str(input())
revise = 0
len_str = len(s)
for i in range(len_str):
    if s[i] != t[i]:
        revise += 1
print(int(revise))