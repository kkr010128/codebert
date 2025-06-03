N = int(input())
s = input()
ans = min(s.count('R'), s.count('W'), s[N-s.count('W'):].count('R'))
print(ans)