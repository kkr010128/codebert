n = int(input())
S = list(map(int,input().split(' ')))
q = int(input())
T = list(map(int,input().split(' ')))

C = 0

for i in S:
    if i in T:
        C += 1
        T.remove(i)
        
print(C)

