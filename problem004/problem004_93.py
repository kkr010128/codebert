def main():
    n = int(input())
    while True:
        try:
            num_list = [int(i) for i in input().split()]
            num_list = sorted(num_list)
            a,b,c = num_list[0],num_list[1],num_list[2]
            if (a**2 + b**2) == c**2:
                print("YES")
            else:
                print("NO")
        except EOFError:
            break
    return None

if __name__ == '__main__':
    main()