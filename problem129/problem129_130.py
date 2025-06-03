N = int(input())
As = sorted(list(map(int, input().split())))

sieve = [True] * 1000001

prev = 0

for i in range(N):
    if As[i] == prev:
        sieve[As[i]] = False
        continue
    else:
        prev = As[i]
        try:
            for j in range(2, 1000000 // prev + 1):
                sieve[prev * j] = False
        except:
            continue

count = 0
As = list(set(As))
for i in range(len(As)):
    if sieve[As[i]] is True:
        count += 1
        
print(count)