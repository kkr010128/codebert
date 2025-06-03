def main():
    n = int(input())
    s = input()
    for i in s:
        mod = (ord(i) - ord('A') + n) % 26
        ans = chr(ord('A') + mod)
        print(ans, end='')
        
if __name__ == '__main__':
    main()