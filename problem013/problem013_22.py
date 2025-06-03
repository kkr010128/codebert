N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

mins = [a[0]]
for i in range(1, N):
    mins.append(min(a[i], mins[i-1]))
    
mx = -10**12
for j in range(1, N):
    mx = max(mx, a[j] - mins[j-1])
print(mx)