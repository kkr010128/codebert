def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    inset = set(inlis)

    if len(inlis) == len(inset):
        print("YES")
    else:
        print("NO")
    
    
if __name__ == "__main__":
    main()
