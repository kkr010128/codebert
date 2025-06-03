a= int(input())
b = list(map(int,input().split()))
b = list(map(lambda x : x-1,b))

bukas = [[]for i in range(a)]
for i in range(1,a):
    bukas[b[i-1]].append(i)
for c in bukas:
    print(len(c))