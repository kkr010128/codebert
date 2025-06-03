# encoding=utf-8
n = int(raw_input())

min = int(raw_input())  
keep = int(raw_input()) 
diff = keep - min       
if keep > min:
    keep = min
n = n - 2

for i in range(n):
    v = int(raw_input())
    if v - keep > diff:
        diff = v - keep
        min = keep
    elif keep > v:
        keep = v

print diff