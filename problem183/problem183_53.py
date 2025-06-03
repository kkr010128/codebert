def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
n=int(input())
nlist=make_divisors(n)
n1list=make_divisors(n-1)
# print(nlist)
# print(n1list)
answer=len(n1list)-1#1を除きます
for i in nlist[1:len(nlist)]:
    pra=n
    while (pra%i==0):
        pra=pra/i
    if pra%i==1:
        answer+=1
print(answer)
