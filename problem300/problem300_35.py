def make_divisors(n):
    from collections import deque
    divisors = deque([])
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    lst_divisors = list(divisors)
    lst_divisors.sort()
    return lst_divisors

a, b = map(int,input().split())

ya = set(make_divisors(a))
yb = set(make_divisors(b))

cand = list(ya&yb)
cand.sort()

#print(cand)

ans = []
if len(cand) > 1:
    for n in cand[1:]:
        if ans:
            for n in cand[1:]:
                for waru in ans:
                    if n%waru == 0:
                        break
                else:
                    ans.append(n)
        else:
            ans.append(n)
#print(ans)
print(len(ans)+1)