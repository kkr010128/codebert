moji = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
memo = {}
for i in range(len(moji)):
    memo.setdefault(moji[i],i)
#print(memo)
n = int(input())
s = str(input())
ans = ''
for i in range(len(s)):
    ans += moji[(memo[s[i]]+n)%26]
print(ans)