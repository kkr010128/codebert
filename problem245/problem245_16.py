# 140 B

n = int(input())
s = input()
num = 0

for i in range(len(s)):
    if s[i] == 'A':
        try:
            if s[i + 1] == 'B' and s[i + 2] == 'C':
                num += 1
        except:
            pass

print(num)