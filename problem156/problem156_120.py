X = int(input())
y =10**5
a ={i**5 for i in range(-y,y)}
ans_a =0
ans_b =0
for b in range(-y,y):
    if X +b**5 in a:
        #ans_a =int( (X +b**5 +1)**0.2 )
        if X +b**5 >0:
            ans_a =int( (X +b**5 )**0.2 )
        else:
            ans_a = -int( abs(X +b**5 )**0.2 )
        ans_b =b
        break
print(ans_a,ans_b)