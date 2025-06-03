A = []
A += map(int, input().split())
A += map(int, input().split())
A += map(int, input().split())
N = int(input())
for _ in range(N):
    b = int(input())
    try:
        A[A.index(b)] = 0
    except ValueError:
        pass
res = (
    (A[0]+A[1]+A[2])*(A[3]+A[4]+A[5])*(A[6]+A[7]+A[8])*
    (A[0]+A[3]+A[6])*(A[1]+A[4]+A[7])*(A[2]+A[5]+A[8])*
    (A[0]+A[4]+A[8])*(A[2]+A[4]+A[6])
)
print("Yes" if res == 0 else "No")
