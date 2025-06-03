s = str(input())
num = 0
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        num += 1
print(num)