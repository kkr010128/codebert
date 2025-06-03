H,A = map(int,input().split())
count = 0
a = 100
while a > 0 :
    a = H - A 
    count += 1
    if a <= 0 :
        break
    else :
        H = a
print(count)