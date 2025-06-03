import sys

def draw_line(chk, W):
    print(chk * int(W / 2) +(chk[0] if W % 2 else ''))
    
def draw(H, W):
    for i in range(H):
        draw_line(['#.', '.#'][i % 2], W)
    print()
    
for line in sys.stdin:
    H, W = map(int, line.split())
    if H == W == 0:
        break
    draw(H, W)