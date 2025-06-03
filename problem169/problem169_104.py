
def main():
    n = int(input())
    a = list(map(lambda i:int(i)-1, input().split(" ")))
    d = {}
    for i in range(n):
        d[i]=0
    for i in range(n-1):
        d[a[i]] += 1
    for i in range(n):
        print(d[i])

if __name__ == "__main__":
    main()