import sys
input = sys.stdin.readline
from collections import deque

def main():
    N, D, A = map(int, input().split())
    monsters = sorted([list(map(int, input().split())) for _ in range(N)])
    
    for i in range(N):
        monsters[i][1] = (monsters[i][1] + A - 1) // A
    
    attacks = deque([]) # [(有効範囲, 攻撃回数)]
    ans = 0
    atk = 0
    for i in range(N):
        atk_this = monsters[i][1]
        while attacks and monsters[i][0] > attacks[0][0]:
            _, atk_ = attacks.popleft()
            atk -= atk_
        if atk_this - atk > 0:
            ans += atk_this - atk
            attacks.append((monsters[i][0]+2*D, atk_this-atk))
            atk += atk_this - atk
    print(ans)
    
if __name__ == '__main__':
    main()
