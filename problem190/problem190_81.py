s = input()
n = len(s)
ans = "No"
cnt = 0
if s[::1] == s[::-1]:
    cnt += 1
if s[:int((n-1)/2):1] == s[int((n-1)/2)-1::-1]:
    cnt += 1
if s[int((n+1)/2)::1] ==  s[:int((n-1)/2):-1]:
    cnt += 1
if cnt == 3:
    ans = "Yes"
print(ans)