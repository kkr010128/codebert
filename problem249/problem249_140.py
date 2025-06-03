A, B, K = map(int, input().split())

if K >= A+B:
    print("0 0")
elif K <= A:
    print("{} {}".format(A-K, B))
elif K > A:
    print("0 {}".format(B-(K-A)))