A,B,C,K = map(int,input().split())
Current_Sum = 0
if K <= A :
    ans = K
elif K <= (A + B):
    ans = A
else:
    K -= (A + B)
    ans = A - K

print(ans)


