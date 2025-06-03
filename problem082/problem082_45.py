def solve():
    S = input()
    T = input()

    ans = float('inf')
    for i in range(0,len(S)-len(T)+1):
        cnt = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(cnt,ans)
    
    print(ans)

if __name__ == '__main__':
    solve()
