def main():
    a = int(input())
    b = int(input())
    if a == 1 and b == 2 or a == 2 and b == 1:
        print(3)
    elif a == 2 and b == 3 or a == 3 and b == 2:
        print(1)
    elif a == 3 and b == 1 or a == 1 and b == 3:
        print(2)
         
if __name__ == '__main__':
    main()