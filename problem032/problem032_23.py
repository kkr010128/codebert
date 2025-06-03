

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(1, 4):
    nums = [(abs(a - b)) ** i for a, b in zip(A,B)]
    print(sum(nums) ** (1/i))
    if i == 1:
        ans = max(nums)
print(ans)
