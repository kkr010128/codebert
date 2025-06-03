def main():
    a,b,c = map(int, input().split())
    
    ab = [i for i in range(a, b + 1)]
    cnt = 0 #count
    for x in range(len(ab)):
        if c % ab[x] == 0:
            cnt += 1
        else:
            pass
    
    print(cnt)


if __name__ == "__main__":
    main()