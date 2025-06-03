def main():
    k=int(input())
    s=7
    for i in range(10**6):
        if s%k == 0:
            print(i+1)
            break
        s = (s*10+7)%k
    else:
        print(-1)

if __name__ == "__main__":
    main()