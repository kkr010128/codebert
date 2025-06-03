A,B,N= map(int,input().split())
max_num = 0
x = min(B-1,N)
print(int((A*x)/B)-(A*int(x/B)))