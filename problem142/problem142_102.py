n = input()
digit1 = int(n[-1])
ans = ''

if digit1 in {2, 4, 5, 7, 9}:
    ans = 'hon'
elif digit1 in {0, 1, 6, 8}:
    ans = 'pon'
elif digit1 in {3}:
    ans = 'bon'

print(ans)
