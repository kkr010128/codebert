A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())
check1=abs(A-B)
check2=(V-W)*T
print("YES" if check1<=check2 else "NO")
