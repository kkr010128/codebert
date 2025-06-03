s=set()
l = [0] * ( 10 ** 5 + 1 )
sum=0
N = int(input())
A = list(map(int, input().split()))
for i in range(len(A)):
    l[A[i]] += 1
    s.add(A[i])
    sum += A[i]
Q = int(input())
for i in range(Q):
    B, C = map(int, input().split())
    if l[B] > 0:
        s.add(C)
        sum = sum + l[B] * ( C - B )
        l[C] += l[B]
        l[B] = 0
        s.discard(B)
    print(sum)
