x, y, z = map(int, raw_input().split())
cnt = 0
for i in range(x, y+1):
    if z%i == 0:
       cnt += 1
    
print cnt