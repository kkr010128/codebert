a, b, c = map(int, raw_input().split(' '))
num = 0
for i in range(a,b+1):
    if c % i == 0:
        num = num + 1
 
print(num)