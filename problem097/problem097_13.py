def main2():
    K = int(input())

    rem = set()
    n = ans = 0

    while True:
        n = n * 10 + 7
        ans += 1

        if n % K == 0:
            print(ans)
            break
        else:
            n = n % K
            
            if n in rem:
                print(-1)
                break
            else:
                rem.add(n)
                
if __name__ == "__main__":
    main2()