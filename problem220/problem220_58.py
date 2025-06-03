def ABC_154_A():
    S,T = map(str, input().split())
    A,B = map(int, input().split())
    U = input()

    if U == S:
        print(str(A-1)+' '+str(B))
    else:
        print(str(A)+' '+str(B-1))

if __name__ == '__main__':

    ABC_154_A()