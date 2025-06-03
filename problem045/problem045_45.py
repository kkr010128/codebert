if __name__ == "__main__":
    a,b = map(int,input().split())
    d,r,f = a/b,a%b,float(a/b)
    print("%d %d %0.5f"%(d,r,f))