def main():
    n = input()
    S = map(int,raw_input().split())
    q = input()
    T = map(int,raw_input().split())
    m = 0
    for i in range(q):
        t = T.pop()
        for j in range(n):
            s = S[j]
            if t == s:
                m += 1
                break
                
    print m

if __name__ == "__main__":
    main()