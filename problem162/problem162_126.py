#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def main():
    n , m = map(int , input().split())
    if n % 2 == 0:
        n -= 1
    k = (n + 1) // 2
    j = 1

    while j < k and m > 0:
        print(j , k)
        j += 1
        k -= 1
        m -= 1

    j = (n + 1) // 2 + 1
    k = n

    while j < k and m > 0:
        if k <= n:
            print(j , k)
            m -= 1
        j += 1
        k -= 1
    
    return

if __name__ == "__main__":
    main()