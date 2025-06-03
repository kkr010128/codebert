def main():
    n = int(input())
    if n%2==1:
        print(0)
    else:
        ans = 0
        waru = 10
        while n>=waru:
            ans += n//waru
            waru = waru*5
        print(ans)
    
if __name__ == "__main__":
    main()
