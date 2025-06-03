# coding:utf-8

def main():
    N = int(input().rstrip())

    for i in range(N):
        ls = list(map(int, input().split(' ')))
        ls.sort()

        if(ls[0]**2 + ls[1]**2 == ls[2]**2):
            print('YES')
        else:
            print('NO')
            
if __name__ == "__main__":
    main()