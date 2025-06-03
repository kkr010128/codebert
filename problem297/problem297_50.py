def ABC_142_A():
    N = int(input())
    guusuu=0
    for i in range(N+1):
        if i%2 == 0 and i !=0:
            guusuu+=1

    print(1-(guusuu/N))




if __name__ == '__main__':

    ABC_142_A()