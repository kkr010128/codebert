import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    S = input()
    T = input()

    #TがSの部分文字列になるようにSを書き換える

    N = len(S)
    M = len(T)
    L = N - M #Sを調べるループの回数
    #二重ループが許される
    ans = M
    for i in range(L+1): 
        #最大M個一致していない。
        cnt = M
        for j in range(M):
            if S[i+j] == T[j]: 
                cnt -= 1
        #最小を取る
        ans = min(ans, cnt)
    print(ans)
if __name__ == '__main__':
    main()
