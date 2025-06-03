n,q = map(int,input().split())
name = []
time = []
for i in range(n):
    a = input().split()
    name.append(a[0])
    time.append(int(a[1]))
s = 0
while name:
    if time[0]> q:
        time[0] -= q
        time.append(time.pop(0))
        name.append(name.pop(0))
        s += q
    else:
        s += time[0] 
        time.pop(0)
        print(name.pop(0),s)