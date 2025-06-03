n  = int(input())
h = [2,4,5,7,9]
p = [0,1,6,8]
b = [3]
t = n%10
if t in h:
    print("hon")
elif t in p:
    print("pon")
else:
    print("bon")