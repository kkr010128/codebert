l, r, d = map(int, input().split(' '))

count = 0

while(l <= r):
    
    if(l % d == 0):
        count += 1
    
    l += 1

print(count)