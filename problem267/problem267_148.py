def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input()

    import re
    num_li = [False]*1000
    for i in range(10):
        first_ = S.find(str(i),0,N-2)
        if first_==-1:
            continue
        for j in range(10):
            second_ = S.find(str(j),first_+1,N-1)
            if second_==-1:
                continue
            for k in range(10):
                third_ = S.find(str(k),second_+1,N)
                if third_==-1:
                    continue
                num_li[i*100+j*10+k]=True
            
    print(sum(num_li))

if __name__=='__main__':
    main()