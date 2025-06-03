n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort()
# print(s)
m = 1
cnt = [1]
ans = []
for i in range(1,n):
    if s[i] == s[i-1]:
        cnt[-1] += 1
    else:
        if cnt[-1] > m:
            ans = [s[i-1]]
        elif cnt[-1] == m:
            ans.append(s[i-1])
        m = max(m, cnt[-1])
        cnt.append(1)
    if i == n-1 and cnt[-1] > m:
        ans = [s[i]]
    elif i == n-1 and cnt[-1] == m:
        ans.append(s[i])
print('\n'.join(ans))