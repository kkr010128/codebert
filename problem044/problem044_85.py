def main():
    a, b, c = map(int,input().split())
 
    _set = set()
    if a <= c and b >= c: _set.add(c)
    if c // 2 < b:
        b = c // 2
    if c % 2 == 0:
        _set = _set | set(range(a, b+1))
    else:
        if a % 2 == 0:
            _set = _set | set(range(a+1, b+1, 2))
        else:
            _set = _set | set(range(a, b+1, 2))
             
    print(sum(map(lambda x: c % x == 0, _set)))
 
main()