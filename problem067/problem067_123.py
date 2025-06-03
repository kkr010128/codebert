n = int(input())
tp = 0
hp = 0
for i in range(n):
    tarou, hanako = map(str,input().split())
    if(tarou > hanako):
        tp += 3
    elif(tarou < hanako):
        hp += 3
    else:
        tp += 1
        hp += 1
print("%d %d" %(tp,hp))
