s,e,bai = [int(x) for x in input().split()]
count=0

for i in range(s,e+1):
    if i%bai == 0:
        count +=1
print(count)