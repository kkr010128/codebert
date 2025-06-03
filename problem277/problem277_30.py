
def main():
    h,w,_ = map(int,input().split())
    ls = [list(input()) for _ in range(h)]
    check = [False for _ in range(h)]


    for i in range(h):
        flg = False
        for j in range(w):
            if ls[i][j] == "#":
                flg = True
        if flg:
            check[i] = True


    ans = [[0 for _ in range(w)] for _ in range(h)]
    now = 1
    for i,flg in enumerate(check):
        if flg:
            ball = False
            for j in range(w):
                if ball == True and ls[i][j]=="#":
                    now +=1
                    ans[i][j]=now
                elif ball == False and ls[i][j]=="#":
                    ans[i][j]=now
                    ball = True
                else:
                    ans[i][j]=now
            now += 1


        else:
            pass
    

    for i,flg in enumerate(check):

        if flg:
            pass

        else:
            k = i
            while 1:
                if k == h-1 and check[h-1]==False:
                    break

                if check[k]:
                    break
                else:
                    k += 1

            for j in range(w):
                ans[i][j] = ans[k][j]
        
    if check[-1]==False:
        index = 0
        for i in range(h):
            if check[i]==True:
                index = i
            else:
                pass

        for i in range(index+1,h):
            for j in range(w):
                ans[i][j]=ans[index][j]


    for i in range(h):
        for j in range(w):
            print(ans[i][j],end=" ")
        print("\n")

if __name__ == "__main__":
    main()