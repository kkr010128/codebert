n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

S.append(-1)
sum = 0
for i in T:
    count = 0
    while True:
        if i != S[count]:
            count += 1
        else:
            sum += 1
            break
        if S[count] == -1:
            break
print(sum)