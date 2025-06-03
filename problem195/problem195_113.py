def main():

    K = int(input())
    a = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
    b = a.split(", ")
    print(b[K-1])
    

    return

if __name__ == '__main__':
    main()