N = int(input())
C = input()

W_total = C.count("W")
R_total = N - W_total
w_cur = 0
r_cur = R_total
ans = R_total
cur = 0

for i in range(N):
    if C[i] == "W":
        w_cur += 1
    else:
        r_cur -= 1

    ans = min(ans, min(w_cur, r_cur) + abs(w_cur - r_cur))

print(ans)