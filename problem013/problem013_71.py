n = int(raw_input())

_min, dif = 10**10, -10**10
for x in xrange(n):
    a = int(raw_input())
    if a -_min > dif:
        dif = a - _min
    if a < _min:
        _min = a
print dif