def main():
    x = input()
    x1, x2, x3 = x.split(' ') 
    a = int(x1)
    b = int(x2)
    c = int(x3)
    if a < b < c:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()