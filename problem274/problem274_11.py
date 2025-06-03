
def main(n,m,s):

    #i初期化
    i = n
    tmp = []
    while i > 0 :
        for j in range(m,-1,-1):
            if j == 0 :
                i = -1
                break

            if i-j >= 0 :
                if s[i-j] == '0':
                    i -= j
                    tmp.append(j)
                    break
    if i == 0:
        for l in reversed(tmp):
            print(l,end=' ')
    else:
        print(-1)


n,m = map(int,input().split())
s = input()
main(n,m,s)
