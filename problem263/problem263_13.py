N = int(input())
A = ''.join(list(map(lambda x: format(int(x), '060b'), input().split(' '))))
mod = 10 ** 9 + 7
ans = 0
for n in range(60):
    one = A[59-n::60].count('1')
    ans = (ans + 2**n *one*(N-one))%mod
print(ans)