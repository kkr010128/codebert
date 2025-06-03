n = int(input())

nums = list(map(int, input().split()))

result = "APPROVED"
for num in nums:
    if (num % 2 == 0) and not ((num % 3 == 0) or (num % 5 == 0)):
        result = "DENIED"
        break

print(result)