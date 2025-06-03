import sys

def f(x,y):
    return x-y,x+y

def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i],y[i] = map(int,input().split())
    f0 = [0]*n
    f1 = [0]*n
    for i in range(n):
        f0[i],f1[i] = f(x[i],y[i])
    print(max(max(f0)-min(f0),max(f1)-min(f1)))

if __name__ == "__main__":
    main()