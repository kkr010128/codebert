if __name__ == "__main__":
    A,B = map(int,input().split())
    for i in range(1,1251):
        A_tmp,B_tmp = int(i*0.08),int(i*0.10)
        if A is A_tmp and B is B_tmp:
            print(i)
            exit()
    print(-1)