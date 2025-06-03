N = int(input())
A = list(map(int, input().split()))
y = sorted([(i+1, A[i]) for i in range(N)], key=lambda x: x[1])
print(" ".join(map(str, [z[0] for z in y])))
