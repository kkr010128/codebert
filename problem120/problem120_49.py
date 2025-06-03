L, R = input().split()
huga = list(map(int, input().split()))
i=0
gou=0

huga.sort()
for a in range(int(R)):
    gou=gou+huga[i]
    i+=1
print(gou)