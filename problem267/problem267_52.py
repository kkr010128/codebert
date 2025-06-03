N = input()
S = list(map(int, input()[:]))
ans = 0
for num in range(1000):
    n1,n2,n3 = 0, 0, num%10
    n2= (num %100-n3)// 10
    n1 = (num-n2*10- n3) //100
    f1 = False
    f2 = False
    f3 = False
    for n in S:
        if not f1:
            if n == n1:
                f1 = True
        elif not f2:
            if n == n2:
                f2 = True
        elif not f3:
            if n == n3:
                f3 = True
                break
    if f1 and f2 and f3:
        ans += 1
print(ans)
