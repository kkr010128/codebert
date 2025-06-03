def main():
    n = int(input())
    al = []
    bl = []
    for _ in range(n):
        a, b = map(int, input().split())
        al.append(a)
        bl.append(b)
    als = list(sorted(al))
    bls = list(sorted(bl))
    if n%2:
        print(bls[n//2]-als[n//2]+1)
    else:
        print(bls[n//2-1]+bls[n//2]-als[n//2]-als[n//2-1]+1)

if __name__ == "__main__":
    main()