n, k = [int(x) for x in input().split()]

a_list = [int(x) for x in input().split()]
a_list.sort()

mod = 10 ** 9 + 7

temp_list = [1] * (n + 1)
for i in range(1, n + 1):
    temp_list[i] = i * temp_list[i - 1] % mod

i_temp_list = [1] * (n + 1)
i_temp_list[-1] = pow(temp_list[-1], mod - 2, mod)
for i in range(n, 0, -1):
    i_temp_list[i - 1] = i_temp_list[i] * i % mod

y = k - 1

ans = 0
for i in range(k - 1, n):
        x = i
        num = temp_list[x] * i_temp_list[y] * i_temp_list[x - y] % mod
        ans += a_list[i] * num % mod
for i in range(n - k + 1):
        x = n - 1 - i
        num = temp_list[x] * i_temp_list[y] * i_temp_list[x - y] % mod
        ans -= a_list[i] * num % mod

ans %= mod
print(ans)