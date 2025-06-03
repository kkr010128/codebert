N, M =map(int,input().split())

A = list(map(int, input().split()))

# x = 宿題をする日の合計
x = sum(A)

if N >= x:
    print(N - x)
else:
    print("-1")



