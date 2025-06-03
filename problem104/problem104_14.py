def main():
    l, r, d = map(int, input().split())
    res = r // d - (l-1) // d
    print(res)

if __name__ == '__main__':
    main()
