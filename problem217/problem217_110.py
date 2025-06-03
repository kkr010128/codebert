N = int(input())
nums = map(int, input().split(" "))

for n in nums:
    if n % 2 != 0:
        continue

    if n % 3 == 0 or n % 5 == 0:
        continue
    else:
        print("DENIED")
        exit(0)

print("APPROVED")