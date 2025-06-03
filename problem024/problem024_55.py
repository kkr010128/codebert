# coding: utf-8

n, k = map(int, input().rstrip().split())
w = [0 for _ in range(n)]
for i in range(n):
    w[i] = int(input())
    
# from random import randint
# n = 100000
# k = 10000
# w = [0 for _ in range(n)]
# for i in range(n):
#     w[i] = randint(1, 10000)
# print(w)
count = 0

def check(P):
    m = 0
    ik = 1
    for i in range(n):
        global count
        count += 1
        new = m + w[i]
        if new > P:
            m = w[i]
            ik += 1
            if ik > k:
                return False
        else:
            m = new
    return True

s = max(sum(w)//k, max(w))
e = sum(w)

while True:
    P = (s + e)//2
    # print("s:{}, e:{}, P:{}".format(s, e, P))
    if s == e:
        break
    if check(P):
        e = P
    else:
        s = P + 1
            
        
print(P)
# print(count)