def palin(x):
    #print(x)
    if x == x[::-1]: return True
    return False
 
a = input()
n = len(a)
if palin(a) and palin(a[:int((n-1)/2)]) and palin(a[int((n+3)/2)-1:]):
    print("Yes")
else: print("No")