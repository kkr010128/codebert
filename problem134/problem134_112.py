N = int(input())
arr = list(map(int, input().split()))
result = 1
if 0 in arr:
    result = 0
else:
    for i in arr:
        result *= i
        if result > 10**18:
            result = -1
            break
print(result)