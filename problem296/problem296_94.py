s = input()
k = int(input())

if len(set(s)) == 1:
    print(len(s)*k//2)
    exit()

l = head = 0
now = s[0]
for i in range(len(s)):
    if s[i] == now:
      head += 1
    else:
        l = i
        break
        
r = tail = 0
now = s[-1]
for i in range(len(s))[::-1]:
    if s[i] == now:
        tail += 1
    else:
        r = i+1
        break

ans = 0
cnt = 0
now = s[l]
for i in range(l,r):
    if s[i] == now:
        cnt += 1
    else:
        ans += cnt//2
        cnt = 1
        now = s[i]
ans += cnt//2
ans *= k

if s[0] == s[-1]:
    ans += (head+tail)//2*(k-1)
    ans += head//2+tail//2
else:
    ans += (head//2+tail//2)*k
print(ans)