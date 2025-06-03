n = int(input())
s, t = list(input().split(' '))
print(''.join([a+b for a,b in list(zip(s, t))]))