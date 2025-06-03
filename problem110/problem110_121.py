from itertools import product


def abc173c_h_and_v():
    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]
    cnt = 0
    for hp in product(range(2), repeat=h):
        for wp in product(range(2), repeat=w):
            a = [c[i][j] for j in range(w) if wp[j] == 1 for i in range(h) if hp[i] == 1]
            if k == a.count('#'):
                cnt += 1
    print(cnt)

abc173c_h_and_v()