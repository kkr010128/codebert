if __name__ == "__main__":
    r = int(input())
    if (1 <= r <= 100) == False:
        print("error")
        exit(1)

    print (r ** 2)