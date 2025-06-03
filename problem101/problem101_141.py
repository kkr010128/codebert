A,B,C = map(int,input().split())
K = int(input())

count = 0

for i in range(K+1):
    if C <= B:
        C *= 2
        count += 1
    elif B <= A:
        B *= 2
        count += 1



if count <= K:
    print('Yes')
else:
    print('No')
