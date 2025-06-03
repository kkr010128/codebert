n = int(input())
s, t = input().split()
s_and_t = s[0]

for i in range(len(s)):
    if(i >= 1):
        s_and_t += s[i]
    s_and_t += t[i]

print(s_and_t)
