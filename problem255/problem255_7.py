n = int(input())
s,t = input().split()

val = ''
for i in range(len(s)):
    val += s[i] + t[i]
print(val)