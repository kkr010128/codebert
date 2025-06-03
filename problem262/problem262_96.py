from typing import List

# 人iの証言を人jに対する証言をリストで格納。1:正直者, 0:不親切, -1:言及なし
def io_info() -> List[List[int]]:
    N = int(input())
    res = [[-1] * N for _ in range(N)]
    for n in range(N):
        a = int(input())
        for _ in range(a):
            x, y = map(int, input().split())
            res[n][x-1] = y
    return res


def main():
    infos = io_info()
    n = len(infos)
    ans = 0
    for i in range(1 << n):
        d = [0] * n
        for j in range(n):
            # iのj+1ビット目が1かどうか,d[j]が正直なら1を割り当てる
            if (i >> j) & 1:
                d[j] = 1
        ok = True
        for j in range(n):
            if d[j]:
                for k in range(n):
                    if infos[j][k] == -1: continue
                    if infos[j][k] != d[k]: ok = False

        if ok: ans = max(ans, bin(i).count("1"))
    print(ans)



if __name__ == '__main__':
    main()
