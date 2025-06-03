import sys
input = sys.stdin.readline

def main():
    N = int(input())
    c = input()
    cnt_r = 0
    cnt_w = 0
    for i in c:
        if i == 'R':
            cnt_r += 1
        else:
            cnt_w += 1
    
    w_left = 0
    r_right = cnt_r
    ans = N
    for i in range(N):
        ans = min(ans, max(w_left, r_right))

        if c[i] == 'W':
            w_left += 1
        else:
            r_right -= 1
    print(min(ans, max(w_left, r_right)))

main()