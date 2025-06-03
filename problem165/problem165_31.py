N = int(input())
s = {}
for i in range(N):
    item = input()
    if item not in s:
        s[item] = 1
print(len(s))