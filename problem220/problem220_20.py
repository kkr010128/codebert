def main():
    s, t = input().split()
    a, b = list(map(int, input().split()))
    u = input()
    
    if s == u:
        a -= 1
    if t == u:
        b -= 1
    print(a,b)
    
if __name__ == '__main__':
    main()