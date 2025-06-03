def main():
    import bisect
    x,y,a,b,c = map(int,input().split())
    p = sorted(list(map(int,input().split())))[-1*x:]
    q = sorted(list(map(int,input().split())))[-1*y:]
    r = sorted(list(map(int,input().split())))
    ans = p+q+r
    ans = sorted(ans,reverse=True)[0:x+y]
    print(sum(ans))

    
if __name__ == "__main__":
    main()
