def main():
    a, b = map(lambda x: int(x.replace('.','')), input().split())
    print(a*b//100)

if __name__ == '__main__':
    main()