def main():
    S=int(input())

    mod=10**9+7

    resList=[1,0,0,1,1,1]
    n=6
    if S>=n:
        for i in range(n,S+1):
            resList.append(resList[i-1]+resList[i-3])
        print(resList[len(resList)-1]%mod)
    else:
        print(resList[S])




if __name__=="__main__":
    main()