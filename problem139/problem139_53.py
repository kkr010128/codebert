import datetime
h,m,eh,em,k = map(int,input().split())
start = h*60 + m
end = eh*60 + em
if end - start > k:
    print(end - k - start)
else:
    print(0)