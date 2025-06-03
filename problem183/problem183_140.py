def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors[1:]

n = int(input())

a = make_divisors(n-1)

b = make_divisors(n)
count = 0

for kk in b:
    mom = n
    while mom % kk == 0:
        mom //= kk
    if mom % kk == 1:
        count +=1

print(len(a) + count)
