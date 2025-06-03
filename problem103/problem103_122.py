N = int(input())
A = list(map(int, input().split()))

ans = 0

lst = [1000] * (N)

for i in range(N): #買うところを選択
    a = A[i]
    for j in range(i + 1, N):
        if A[j] > a:
            tmp = lst[i] // a * A[j] + lst[i] % a
            lst[j] = max(max(lst[j], tmp), lst[j - 1])
        else:
            lst[j] = max(lst[j], lst[j - 1])

print (lst[-1])
# print (lst)