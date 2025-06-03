n = int(input())
S = set(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

sum = 0

for i in T:
    if i in S:
        sum +=1
        
print(sum)