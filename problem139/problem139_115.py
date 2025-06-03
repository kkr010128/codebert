def main():
    h1, m1, h2, m2, k = map(int, input().split())
    a = h1*60+m1
    b = h2*60+m2
    print(b-a-k)

if __name__ == "__main__":
    main()