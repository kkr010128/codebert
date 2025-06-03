n = int(input())
s = input()

num = len(s)
ans = s.count('R')*s.count('G')*s.count('B')

for i in range(num):
    for j in range(i+1, num):
        if 0 <= 2*j-i < num:
            if s[i] != s[j] and s[j] != s[2*j-i] and s[2*j-i] != s[i]:
                ans -= 1
print(ans)
