import sys
prime = lambda x: True if x==2 else False if x<2 or not x%2 else pow(2,x-1,x)==1
inp = sys.stdin.readlines()
print(len([prime(e) for e in list(map(int, inp[1:])) if prime(e)==1]))