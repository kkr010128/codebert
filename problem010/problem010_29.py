_n = int(raw_input())
_a = [int(x) for x in raw_input().split()]

for i in range(1, _n):
    print(" ".join([str(x) for x in _a]))
    key = _a[i]
    j = i - 1
    while j >= 0 and _a[j] > key:
        _a[j+1] = _a[j]
        j -= 1
    _a[j+1] = key
        
print(" ".join([str(x) for x in _a]))