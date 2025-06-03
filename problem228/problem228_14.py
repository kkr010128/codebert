H = int(input())
Ans = 0
n = 0
while True:
    if H != 1:
        H = H//2
        Ans += 2**n
        n += 1
    else:
        Ans += 2**n
        break
print(Ans)