def main3():
    N, A, B = map(int, input().split())
    
    d = B - A
    if d % 2 == 0:
        print(d // 2)
    else:
        print(min(((d + 1) // 2 + N - B ), ((d + 1) // 2 + A - 1)))
         
if __name__ == "__main__":
    main3()