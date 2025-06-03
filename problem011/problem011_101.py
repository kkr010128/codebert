num_list = raw_input().split()
num_list = map(int, num_list)

def gcd(x, y): 
    if x < y:
        x, y = y, x
    while (y>0):
        r = x % y 
        x = y 
        y = r 

    return x

x = num_list[0]
y = num_list[1]

print gcd(x, y)