n,k,c = map(int, input().split())
s = input()
L = []
L.append(-c)
workday = 1
for i in range(1, n+1):
    if i <= L[workday-1] + c:
        continue
    if s[i-1] == 'x':
        continue
    L.append(i)
    workday += 1
    if workday == k + 1:
        break
R = [0] * (k+2)
R[k+1] = n + c + 1
workday = k
for i in range(n, 0, -1):
    if i >= R[workday+1] - c:
        continue
    if s[i-1] == 'x':
        continue
    R[workday] = i
    workday -= 1
    if workday == 0:
        break
for i in range(1, k+1):
    if L[i] == R[i]:
        print(L[i])