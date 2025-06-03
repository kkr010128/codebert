n,q = map(int,input().split())
process = []
for i in range(n):
    name,time = input().split()
    process.append([name,int(time)])
elap = 0
out = []
while len(process) > 0:
    name,time = process.pop(0)
    temp_q = q
    while True:
        if time <= 0:
            out.append([name,elap])
            break
        if temp_q <= 0:
            process.append([name,time])
            break
        time -= 1
        temp_q -= 1
        elap += 1
for name,time in out:
    print(name,time)
