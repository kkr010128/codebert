n,q = map(int,input().split())
name = []
time = []
for i in range(n):
    tmp = input().split()
    name.append(str(tmp[0]))
    time.append(int(tmp[1]))
    
total = 0
result = []
while True:
    try:
        if time[0] > q:
            total += q
            time[0] = time[0] - q
            tmp = time.pop(0)
            time.append(tmp)
            tmp = name.pop(0)
            name.append(tmp)
        elif q >= time[0] and time[0] > 0:
            total += time[0]
            time.pop(0)
            a = name.pop(0)
            print(a,total)
        else:
            break
    except:
        break