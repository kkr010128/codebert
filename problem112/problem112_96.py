MOD = (10 ** 9) + 7
n, k  = map(int, input().split())
a = list(map(int, input().split()))
 
negs = [-x for x in a if x < 0]
non_negs = [x for x in a if x >= 0]
 
if len(non_negs) == 0 and k % 2 == 1:
    negs.sort()
    ans = 1
    for i in range(k):
        ans = ans * -negs[i] % MOD
    print(ans)
    exit()
 
negs_p, non_negs_p = 0, 0
 
negs.sort(reverse = True)
non_negs.sort(reverse = True)
 
for i in range(k):
    if negs_p == len(negs):
        non_negs_p += 1
    elif non_negs_p == len(non_negs):
        negs_p += 1
    elif negs[negs_p] > non_negs[non_negs_p]:
        negs_p += 1
    else:
        non_negs_p += 1
 
if negs_p % 2 == 0 or k == n:
    ans = 1
    for i in range(negs_p):
        ans = ans * -negs[i] % MOD
    for i in range(non_negs_p):
        ans = ans * non_negs[i] % MOD
    print(ans)
    exit()
 
if negs_p == len(negs) or non_negs_p == 0:
    negs_p -= 1
    non_negs_p += 1
    ans = 1
    for i in range(negs_p):
        ans = ans * -negs[i] % MOD
    for i in range(non_negs_p):
        ans = ans * non_negs[i] % MOD
    print(ans)
    exit()
 
if non_negs_p == len(non_negs) or negs_p == 0:
    negs_p += 1
    non_negs_p -= 1
    ans = 1
    for i in range(negs_p):
        ans = ans * -negs[i] % MOD
    for i in range(non_negs_p):
        ans = ans * non_negs[i] % MOD
    print(ans)
    exit()
 
 
a = negs[negs_p - 1]
b = negs[negs_p]
c = non_negs[non_negs_p - 1]
d = non_negs[non_negs_p]
 
if a * b > c * d:
    negs_p += 1
    non_negs_p -= 1
else:
    negs_p -= 1
    non_negs_p += 1
 
ans = 1
for i in range(negs_p):
    ans = ans * -negs[i] % MOD
for i in range(non_negs_p):
    ans = ans * non_negs[i] % MOD
print(ans)