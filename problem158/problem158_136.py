K =int(input())
A,B = map(int,input().split())
q, mod = divmod(A, K)
if mod == 0:
    print("OK")
elif K*(q+1) <= B:
    print("OK")
else:
    print("NG")