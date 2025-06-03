n = int(input())
_s = input()
q = int(input())
query = [input() for _ in range(q)]

def bitsum(_bit, i):
    s = 0
    while i > 0:
        s += _bit[i]
        i -= i & (-i)
    return s

def bitadd(_bit, i, x):
    while i <= n:
        _bit[i] += x
        i += i & (-i)
    return _bit

al = [chr(ord('a') + i) for i in range(26)]
al_to_idx = dict()
for i in range(26):
    al_to_idx[al[i]] = i

s = list(_s)

# init
import math
n_ = int(math.log(n) / math.log(2)) + 1
bit = [[0] * (2 ** n_ + 1) for _ in range(26)]
for i in range(n):
    idx = al_to_idx[s[i]]
    bit[idx] = bitadd(bit[idx], i + 1, 1)
# print(bit)

for i in range(q):
    _query = query[i].split(' ')
    if _query[0] == '1':
        # decrement old
        idx = al_to_idx[s[int(_query[1]) - 1]]
        bit[idx] = bitadd(bit[idx], int(_query[1]), -1)

        s[int(_query[1]) - 1] = _query[2]
        # print(s)

        # increment
        idx = al_to_idx[_query[2]]
        bit[idx] = bitadd(bit[idx], int(_query[1]), 1)

    else:
        _ans = 0
        for idx in range(26):
            _bit = bit[idx]
            c = bitsum(_bit, int(_query[2])) - bitsum(_bit, int(_query[1]) - 1)
            if c != 0:
                _ans += 1
        print(_ans)
