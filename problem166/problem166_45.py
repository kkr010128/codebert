a = input()[::-1]
add = 0
ans = [1] + [0] * 2018
ans_int = 0
d = 1

for i in range(len(a)):
    add = (add + int(a[i]) * d) % 2019
    d = (10 * d) %2019
    ans[add] += 1

for i in range(len(ans)):
    a =((ans[i] - 1) * ans[i]) /2
    ans_int += a

print(int(ans_int))
