x=int(input())

for i in range(int(x**.5),0,-1):
    if x%i==0: break
print(i+x//i-2)