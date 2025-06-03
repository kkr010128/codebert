def main():
    d, t, s = map(int, input().split())
    print("Yes" if d / s <= t else "No") 


if __name__ == "__main__":
    main()