n = int(input())
x = input()

original_pop_count = x.count('1')
one_pop_count = original_pop_count - 1 # 0になりうる
zero_pop_count = original_pop_count + 1

# X mod p(X) += 1 の前計算
one_mod = 0
zero_mod = 0
for b in x:
    if one_pop_count != 0:
        one_mod = (one_mod * 2 + int(b)) % one_pop_count
    zero_mod = (zero_mod * 2 + int(b)) % zero_pop_count

# f の前計算
f = [0] * 220000
pop_count = [0] * 220000
for i in range(1, 220000):
    # pop_count[i] = pop_count[i // 2] + i % 2
    pop_count[i] = bin(i)[2:].count('1')
    f[i] = f[i % pop_count[i]] + 1

for i in range(n-1, -1, -1):
    if x[n-i-1] == '1':
        if one_pop_count != 0:
            nxt = one_mod
            nxt -= pow(2, i, one_pop_count)
            nxt %= one_pop_count
            print(f[nxt] + 1)
        else:
            print(0)
    elif x[n-i-1] == '0':
        nxt = zero_mod
        nxt += pow(2, i, zero_pop_count)
        nxt %= zero_pop_count
        print(f[nxt] + 1)