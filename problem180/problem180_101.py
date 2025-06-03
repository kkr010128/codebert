n,k = map(int,input().split())

if n > 2*k :
    n = n%(2*k)

while True:
    mae = n
    n = abs(k-n)
    if mae <= n:
        break

print(mae)
