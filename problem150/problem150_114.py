N,K = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
B = {1:1}
x = A[1]
st = 0
while True:
    if x not in B:
        B[x] = 1
        x = A[x]
    else:
        st = x
        break
x = 1
t = 0
while x!=st:
    x = A[x]
    t += 1
x = st
x = A[x]
T = 1
while x!=st:
    x = A[x]
    T += 1
if K<=t:
    x = 1
    cnt = 0
    while cnt<K:
        x = A[x]
        cnt += 1
    print(x)
else:
    K -= t
    K = K%T
    x = st
    cnt = 0
    while cnt<K:
        x = A[x]
        cnt += 1
    print(x)