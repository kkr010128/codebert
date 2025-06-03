import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()[0:-1]
# n = int(input())
m1,d1 = map(int, input().split())
m2,d2 = map(int, input().split())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


# ab=[]
# for i in range():
#     a,b = map(int, input().split())
#     ab.append([a,b])


     
def main():
    if m1 ==12:
        if m2 == 1 and d2 ==1 :
            print(1)
        else:
            print(0)
    else:
        if m2 ==m1+1 and d2 ==1:
            print(1)
        else:
            print(0)
        
    
    

if __name__ == '__main__':
    main()