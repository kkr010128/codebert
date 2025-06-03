'''
def main():
    N, D = map(int, input().split(" "))
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split(" "))))
    D2 = D **2
    cnt = 0
    for i in range(N):
        if xy[i][0] **2 + xy[i][1] **2 > D2:
            continue
        cnt += 1
    print(cnt)
'''
#if,contiueの使い方による実行時間の比較用
def main():
    N, D = map(int, input().split(" "))
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split(" "))))
    D2 = D **2
    cnt = 0
    for i in range(N):
        if xy[i][0] **2 + xy[i][1] **2 <= D2:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()