n = int(input())
a = input()
s=list(map(int,a.split()))

q = int(input())
a = input()
t=list(map(int,a.split()))

i = 0
for it in t:
    if it in s:
        i = i+1
print(i)