h = int(input())
w = int(input())
n = int(input())

c = n // max(h,w)
if(n % max(h,w) != 0):c+=1
print(c)