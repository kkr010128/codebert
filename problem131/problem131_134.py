a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if a <= b:
    print('YNEOS'[a+v*t < b+w*t::2])
else:
    print('YNEOS'[a-v*t > b-w*t::2])