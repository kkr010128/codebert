import numpy as np

if __name__ == "__main__":
    N=input()
    N=int(N)
    l=[]
    for i in range(N):
        buf=input()
        l+=[buf]
    l=np.array(l)
    print(len(np.unique(l)))