n = input()
x = input().split()
x_int = [int(i) for i in x]

print('{} {} {}'.format(min(x_int),max(x_int),sum(x_int)))