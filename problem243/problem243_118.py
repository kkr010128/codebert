import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()
n = int(input())
# n,m = map(int, input().split())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


st=[]
for i in range(n):
    s,t = map(str, input().split())
    t = int(t)
    st.append((s,t))

x = input()[0:-1]
     
def main():
    ans = 0
    flag = False

    for i in  st:
        s,t = i
        if flag:
            ans+=t
        if s == x:
            flag = True
        
    print(ans)
    
    

if __name__ == '__main__':
    main()