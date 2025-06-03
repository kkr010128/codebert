def main():
    a,v = map(int,input().split())
    b,w = map(int,input().split())
    t = int(input())
    d = abs(b-a)
    u = v-w
    if u<=0:
        print('NO')
    else:
        if d/u>t:
            print('NO')
        else:
            print('YES')
    
if __name__ == "__main__":
    main()
