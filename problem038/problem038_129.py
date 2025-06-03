#(a,b) = input().rstrip().split(' ')
#a = int(a)
#b = int(b)

#以下でも代替可
(a,b) = [int(x) for x in input().rstrip().split(' ')]

if a < b:
 print("a < b")
elif a > b:
 print("a > b")
else:
 print("a == b")