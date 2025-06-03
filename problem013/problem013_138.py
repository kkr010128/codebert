n = int(raw_input())
a = []
a.append(int(raw_input()))
Min = a[0]
Max = -1*10**9
for j in range(1,n):
    a.append(int(raw_input()))
    Max = max(Max,a[j]-Min)
    Min = min(Min,a[j])
print Max