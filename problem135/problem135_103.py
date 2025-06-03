def main():
    a,b = input().split()
    b = b[0] + b[2:]
    print(int(a)*int(b)//100)

if __name__ == "__main__":
    main()
