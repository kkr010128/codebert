def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    anslis = [0] * n
    for i in range(n):
        num = inlis[i]
        anslis[num-1] = i+1
    print(*anslis)
    
if __name__ == "__main__":
    main()
