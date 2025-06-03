def main():

    N, A, B = map(int, input().split())
    if (B-A) % 2 == 0:
        return  (B-A) // 2
    else:
        a = A-1 + (B-A+1)//2
        b = N-B+1 + (B-A-1) // 2
        return min([a, b])

if __name__ == '__main__':
    print(main())
