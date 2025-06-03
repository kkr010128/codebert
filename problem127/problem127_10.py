def sol():
    x, y = map(int, input().split())
    for i in range(x+1):
        for j in range(x+1):
            if (i+j) == x and 4*i + 2*j == y:
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    sol()
