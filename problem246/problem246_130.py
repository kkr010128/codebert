n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

def factorial(n) :
    if n == 1:
        return 1
    else :
        return n*factorial(n-1)

num_p = 0
num_q = 0
for i in range(n-1) :
    sort_p = sorted(p[i:],reverse=True)
    index_p = sort_p.index(p[i])
    mp = n - (index_p + 1)
    num_p += mp * factorial(n-(i+1))

    sort_q = sorted(q[i:],reverse = True)
    index_q = sort_q.index(q[i])
    mq = n - (index_q + 1)
    num_q += mq * factorial(n-(i+1))

print(abs(num_p - num_q))
