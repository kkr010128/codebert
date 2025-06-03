n = int(input())
a = list(map(int, input().split()))

num = [0]*(10**6+1)

for x in a:
    num[x] += 1

pairwise = True
for i in range(2, 10**6+1):
    cnt = sum(num[i::i])
    if cnt == n:
        print('not coprime')
        exit()
    if cnt > 1:
        pairwise = False

if pairwise:
    print('pairwise coprime')
else:
    print('setwise coprime')
    
