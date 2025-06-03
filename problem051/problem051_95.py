import sys

tmp = '#.' * 151

def draw(H, W):
    odd = tmp[:W]
    even = tmp[1:W + 1]
    print((odd + '\n' + even + '\n') * (H // 2) + (odd  + '\n' if H % 2 else ''))
    
for line in sys.stdin:
    H, W = map(int, line.split())
    if H == W == 0:
        break
    draw(H, W)