N = int(input())
n =10**9 + 7
a = (10**N) % n
b = (9**N) % n
c = (8**N) % n

x = (a - 2*b + c) % n
print(x)