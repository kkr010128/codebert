def main():
    N = int(input())
    st = [0]*N
    for i in range(N):
        s,t = input().split()
        st[i] = [s,int(t)]
    X = input()
    ans = 0
    flag = False
    for i in range(N):
        if flag:
            ans += st[i][1]
        if st[i][0] == X:
            flag = True
    print(ans)

if __name__ == '__main__':
    main()