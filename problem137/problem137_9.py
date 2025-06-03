N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[(n + 1) // 2 - 1]
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2

med_a = median(A)
med_b = median(B)
if N % 2 == 1:
    ans = int(med_b) - int(med_a) + 1
else:
    ans = med_b * 2 - med_a * 2 + 1
    ans = int(ans)

print(ans)