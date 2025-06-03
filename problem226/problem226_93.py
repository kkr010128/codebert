def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    if H > s:
        print('No')
    else:
        print('Yes')
main()