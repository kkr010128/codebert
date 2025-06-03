#coding: UTF-8

def X_Cubic(x):
    return x*x*x

if __name__=="__main__":
    x = input()
    ans = X_Cubic(int(x))
    print(ans)