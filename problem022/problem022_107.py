n1 = int(input())
a1 = [int(x) for x in input().split()]
n2 = int(input())
a2 = [int(x) for x in input().split()]

res = set()

cnt = 0

for i in range(n1) :
    for j in range(n2) :
        if a1[i] == a2[j] :
            res.add(a1[i])
            
print(len(res))
            
