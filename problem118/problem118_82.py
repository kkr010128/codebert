def main():
    N = int(input())

    def sum_num(num):
        div = N // num
        
        ret = num * int(div * ((1 + div) / 2))
        
        return (ret)

    ans = 0

    for i in range(1, N + 1):
        ans += sum_num(i)

    print(ans)

if __name__ == '__main__':
    main()
