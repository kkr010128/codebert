n, k, c = map(int, input().split())
s = input()

l = []
r = []

res = []


def fun(string, pos):
    counter = 0
    consec_counter = c + 1
    res = []
    while pos < n:
        # print(pos)
        if counter == k:
            break
        if consec_counter >= c and string[pos] == 'o':
            counter += 1
            consec_counter = 0
            res.append(pos)
        else:
            consec_counter += 1
        pos += 1;
    # print(res)
    return res


def invfun(string, pos):
    counter = 0
    consec_counter = c + 1
    res = []
    while pos >= 0:
        if counter == k:
            break
        # print(pos)
        if consec_counter >= c and string[pos] == 'o':
            counter += 1
            consec_counter = 0
            res.append(pos)
        else:
            consec_counter += 1
        pos -= 1;
    # print(res)
    return res


little_res = fun(s, 0)
lres = []
if len(little_res) == k:
    lres = little_res
else:
    exit()

little_res = invfun(s, n - 1)
rres = []
if len(little_res) == k:
    rres = little_res
else:
    exit()
# print(lres)
# print(rres)
for i in range(k):
    if lres[i] == rres[k - 1 - i]:
        print(lres[i] + 1)
