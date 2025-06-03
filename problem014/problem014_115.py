_n = int(raw_input())
_a = [int(x) for x in raw_input().split()]

_flg = 1
cnt = 0

while _flg:
    _flg = 0
    for i in reversed(range(1, _n)):
        if _a[i] < _a[i-1]:
            _a[i], _a[i-1] = _a[i-1], _a[i]
            cnt += 1
            _flg = 1

print(" ".join([str(x) for x in _a]))
print(cnt)