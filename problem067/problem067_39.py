n = int(input())
a = [[i for i in input().split()] for i in range(n)]
taroup = 0
hanakop = 0
for i in range(n):
    array =[]
    array.append(a[i][0])
    array.append(a[i][1])
    array.sort()
    if array[1] == a[i][0] and  array[1] != a[i][1]:
        taroup += 3
    elif array[1] == a[i][1] and  array[1] != a[i][0]:
        hanakop += 3
    elif array[0] == array[1]:
        taroup += 1
        hanakop += 1
print(str(taroup)+" "+str(hanakop))