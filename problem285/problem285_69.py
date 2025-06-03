def main():
    S = input()
    N = len(S)+1
    a = [0]*(N)
    #右側からみていく
    for i in range(N-1):
        if S[i] == '<':
            a[i+1] = max(a[i]+1,a[i+1])
    #print(a)
    #左側から見ていく
    for i in range(N-2,-1,-1):
        #print(i)
        if S[i] == '>':
            a[i] = max(a[i+1]+1,a[i])
    ans = 0
    #print(a)
    for i in range(N):
        ans += a[i]
    return ans

print(main())
