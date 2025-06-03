n = int(input())
a = list(map(int,input().split()))
M = max(a)+1
if M == 2:
    print("pairwise coprime")
    exit()
count = [0]*(M)
prime = [2,3,5,7,11,13]
for i in range(14,int(M**0.5)+2):
    check = True
    for j in prime:
        if i%j == 0:
            check = False
            break
    if check:
        prime.append(i)
 
for i in a:
    for j in prime:
        if i < j:
            break
        if i%j==0:
            while i%j == 0:
                i //= j
            count[j] += 1
    if i > 1:
        count[i] += 1
 
ans = max(count)
 
if ans == 1:
    print("pairwise coprime")
elif ans == n:
    print("not coprime")
else:
    print("setwise coprime")