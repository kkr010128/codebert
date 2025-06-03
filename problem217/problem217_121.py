n = int(input())
a = [int(s) for s in input().split()]

ans = 'APPROVED'

for num in a:
    if num % 2 == 0:
        if num % 3 != 0 and num % 5 != 0:
            ans = 'DENIED'
            break
print(ans)