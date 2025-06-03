N = int(input())

n = N % 10

if n == 3:
    ans = 'bon'
elif n == 0 or n == 1 or n == 6 or n == 8:
    ans = 'pon'
else:
    ans = 'hon'

print(ans)