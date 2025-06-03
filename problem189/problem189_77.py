n, m = map(int, input().split())

def solve(n):
    if n == 0:
        return 1
    return n * solve(n - 1)

if n <= 1:
    n_ans = 0
else:
    n_ans = solve(n) // (solve(n - 2) * 2)
if m <= 1:
    m_ans = 0
else:
    m_ans = solve(m) // (solve(m - 2) * 2)
ans = n_ans + m_ans
print(ans)
