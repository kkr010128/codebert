def main():
    a, b = tuple(map(int,input().split()))
    print(gcd(a, b))

def gcd(x, y):    
    # x > y となるように並べ替え
    if x < y:
        (x, y) = (y, x)
    return x if y == 0 else gcd(y, x%y)

if __name__ == '__main__':
    main()

