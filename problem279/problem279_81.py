def main():
    n = int(input())
    s = input()
    if n % 2 == 0:
        sl = len(s) // 2 
        s1 = s[:sl]
        s2 = s[sl:]
        if s1 == s2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
     
if __name__ == '__main__':
    main()