def main():
    x = int(input())
    total = 100
    for i in range(10**5):
        if total >= x:
            print(i)
            return
        total += total//100

if __name__ == "__main__":
    main()