# input
N = int(input())

# 約数
def getDivs(n):
    divs = [n]
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            divs.append(i)
            if i != n//i:
                divs.append(n//i)
    return divs

# process
if N == 2:
    print(1)
else:
    pf1 = getDivs(N)
    pf2 = getDivs(N-1)
    cnt = len(pf2)

    for x in pf1:
        n = N
        while n%x == 0:
            n //= x
        n %= x 
        
        if n == 1:
            cnt += 1

    # print(pf1)
    # print(pf2)
    print(cnt)
