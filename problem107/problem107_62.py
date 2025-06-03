n = int(input())
x = list(input())

def popcount(n):
    bin_n = bin(n)[2:]
    count = 0
    for i in bin_n:
        count += int(i)
    return count

cnt = 0
for i in range(n):
    if x[i] == '1':
        cnt += 1

plus = [0 for i in range(n)] # 2^index を cnt+1 で割った時のあまり
minus = [0 for i in range(n)] # 2^index を cnt-1 で割った時のあまり
if cnt == 0:
    plus[0] = 0
else:
    plus[0] = 1
if cnt != 1:
    minus[0] = 1
for i in range(1, n):
    plus[i] = (plus[i-1]*2) % (cnt+1)
    if cnt != 1:
        minus[i] = (minus[i-1]*2) % (cnt-1)

origin = int(''.join(x), base=2)
amariplus = origin % (cnt+1)
if cnt != 1:
    amariminus = origin % (cnt-1)

for i in range(n):
    if x[i] == '0':
        amari = (amariplus + plus[n-i-1]) % (cnt+1)
    else:
        if cnt != 1:
            amari = (amariminus - minus[n-i-1]) % (cnt-1)
        else:
            print(0)
            continue
    ans = 1
    while amari != 0:
        ans += 1
        amari = amari % popcount(amari)
    print(ans)