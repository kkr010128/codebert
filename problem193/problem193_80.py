import sys
 
readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)
 
 
def main():
    def divide_choco(bit):
        divrow_num = bin(bit).count("1") + 1  # 割った回数+1
        choco_current = [[0] * w for _ in range(divrow_num)]
 
        row_divided_cur = 0
 
        for col, piece in enumerate(choco[0]):
            choco_current[0][col] = piece
 
        for row in range(h - 1):
            if bit >> row & 1:
                row_divided_cur += 1
            for col, piece in enumerate(choco[row + 1]):
                choco_current[row_divided_cur][col] += piece
 
        return choco_current, divrow_num
 
    h, w, k = list(map(int, readline().split()))
    choco = []
 
    for i in range(h):
        choco_in = input()
        choco_add = [int(c) for c in choco_in]
        choco.append(choco_add)
 
    ans = INF
 
    for bit in range(1 << (h - 1)):
        choco_current, divrow_num = divide_choco(bit)
        choco_cursum = [0] * divrow_num
        is_exceed = False  # 超えてる場合True
 
        ans_temp = bin(bit).count("1")
        if divrow_num > 1:
            for col in range(w):
                choco_currow = [choco_current[dr][col] for dr in range(divrow_num)]
                for drow, pieces in enumerate(choco_currow):
                    if pieces > k:
                        ans_temp += INF
                    elif choco_cursum[drow] + pieces > k:
                        is_exceed = True
 
                if is_exceed:
                    choco_cursum = [cc for cc in choco_currow]
                    ans_temp += 1
                    is_exceed = False
                else:
                    choco_cursum = [cc + cs for cc, cs in zip(choco_currow, choco_cursum)]
        else:
            choco_cursum = 0
            for pieces in choco_current[0]:
                if pieces > k:
                    ans_temp += INF
                elif choco_cursum + pieces > k:
                    choco_cursum = pieces
                    ans_temp += 1
                else:
                    choco_cursum = choco_cursum + pieces
 
        ans = min(ans, ans_temp)
 
    print(ans)
 
 
if __name__ == '__main__':
    main()