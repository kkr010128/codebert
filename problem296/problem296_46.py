S = [i for i in input()]
K = int(input())
ans = 0
s = S*2
for i in range(1,len(s)):
    if s[i-1] == s[i]:
        s[i] = "_"
        if i >= len(s)//2:
            ans += K-1
        else:
            ans += 1
kazu = set(S)
if len(kazu) == 1 and len(S) % 2 != 0:
  ans = len(S) * (K//2) + (K%2==1) * (len(S)//2)
print(ans)