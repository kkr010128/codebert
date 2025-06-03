def main():
    H1, M1, H2, M2, K = map(int, input().split())

    t1 = 60*H1 + M1
    t2 = 60*H2 + M2

    d = 0
    if t1 <= t2:
        d = t2 - t1
    else:
        d = 60*24 - t1 + t2

    print(max(0, d - K))
    
if __name__ == "__main__":
    main()