data = []
while True:
    in_line = raw_input().split()
    n = int(in_line[0])
    x = int(in_line[1])
    if n == 0 and x == 0:
        break
    data.append([n,x])
for n in data:
    count = 0
    for i in range(1,n[0]+1):
        for j in range(i+1,n[0]+1):
            for k in range(j+1,n[0]+1):
                if i+j+k == n[1]:
                    count += 1
    print count