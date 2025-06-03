cnt = 0
pos = 360
muki = int(input())
while pos != 0:
    pos += muki
    pos %= 360
    cnt += 1
print(cnt)    
