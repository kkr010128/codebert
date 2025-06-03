def solve():
    K,X = [int(input_elem) for input_elem in input().split()]
    if K*500 >= X:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()