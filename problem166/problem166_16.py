from sys import stdin, stdout
s = input()
n = len(s)


if len(s) <= 3:
    print(0)
    exit()

suffix_rems = [-1]*n
suffix_rems[-1] = int(s[-1])
suffix_rems[-2] = int(s[-2:])
suffix_rems[-3] = int(s[-3:])

rems_d = dict()
rems_d[0] = 1
rems_d[int(s[-1])] = 1
rems_d[int(s[-2:])] = 1
rems_d[int(s[-3:])] = 1

special_keys = set()
for i in range(n-3)[::-1]:
    rem = (pow(10, n-i-1, 2019) * int(s[i]) + suffix_rems[i + 1])%2019

    if rem in rems_d:
        rems_d[rem] += 1
        special_keys.add(rem)
    else:
        rems_d[rem] = 1

    suffix_rems[i] = rem

ans = 0
for key in special_keys:
    t = rems_d[key]
    ans += (t*(t-1))//2

print(ans)