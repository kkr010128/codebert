n, q = map(int, input().split())
data = []
for i in range(n):
    tmp = input().split()
    tmp[1] = int(tmp[1])
    data.append(tmp)

dt_out = []
time_count = 0

while len(data) > 0 :
    tmp = data.pop(0)
    if(tmp[1] <= q):
        time_count += tmp[1]
        dt_out.append([tmp[0],time_count])
    else:
        tmp[1] -= q
        time_count += q
        data.append(tmp)

for tmp in dt_out:
    print(tmp[0]+" "+str(tmp[1]))