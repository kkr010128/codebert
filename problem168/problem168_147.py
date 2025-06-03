def main():
    n,m = map(int,input().split())
    a = [int(i) for i in input().split()]
    Sum = sum(a)
    if n<Sum:
        print('-1')
    else:
        print(n-Sum)
main()
