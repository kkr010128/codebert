n = input()
S = list(map(int,input().split()))
n = input()
T = list(map(int,input().split()))
count =  0
for i in T:
    if i in S:
        count+= 1
print(count)