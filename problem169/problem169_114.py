n = int(input())
p = list(map(int,input().split()))

p2 = [0]*n 

for x in p:
    p2[x-1] = p2[x-1] + 1

for x in p2:
    print(x)