def base_10_to_n(x, n):
    ans = []
    while x > 0:
        x -= 1
        ans.append(str(x % n + 1))
        x //= n
    return ans[::-1]


a = base_10_to_n(int(input()), 26)
ans1 = ''
for i in a:
    ans1 += chr(ord('a') + int(i) - 1)

print(ans1)
