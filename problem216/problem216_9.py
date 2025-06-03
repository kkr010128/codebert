def main():
    a,b,c = map(int,input().split())
    if a == b and b==c :
        print("No")
        return
    if a != b and b != c and a != c:
        print("No")
        return
    print("Yes")
    return

if __name__ == "__main__":
    main()