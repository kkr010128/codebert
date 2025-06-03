N = int(input())
A = list(map(int, input().split()))

money = 1000
kabu = 0
for i in range(N-1):
    if kabu > 0:
        money += kabu*A[i]
        kabu = 0
    if A[i] < A[i+1]:
        kabu = money//A[i]
        money -= kabu*A[i]
if kabu > 0:
    money += kabu*A[-1]

print(money)
