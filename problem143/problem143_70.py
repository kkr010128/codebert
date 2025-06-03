a = int(input())
b = input()
c = len(b)

if c <= a:
    print(b)
else: 
    print(b[:a] + "...")