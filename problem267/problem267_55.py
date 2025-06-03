N = int(input())
S = input()
ans = 0

passwords = [str(i).zfill(3) for i in range(1000)]
for pw in passwords:
    S_copy = S
    for digit in pw:
        try:
            S_copy = S_copy[S_copy.index(digit)+1:]
        except ValueError:
            break
    else:
        ans += 1

print(ans)

