def main():
    N = int(input())
    A = [ int(a) for a in input().split()]
    A_ = set(A)
    if len(A)==len(A_):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()