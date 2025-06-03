def main():
    H,A = [int(x) for x in input().split()]
    ans = H//A
    if H%A > 0:
        print(ans+1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
