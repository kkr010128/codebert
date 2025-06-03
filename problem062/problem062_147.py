# AOJ ITP1_8_B

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    while True:
        n = int(input())
        if n == 0: break
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        print(sum)

if __name__ == "__main__":
    main()

