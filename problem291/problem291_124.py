def main():
    # n=int(input())
    n,k= map(int, input().split())
    p=n-2*k
    print(p) if p>0 else print(0)
    return
main()