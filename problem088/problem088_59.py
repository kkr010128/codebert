n=int(input())
a=[int(k) for k in input().split()]

sum=0;
max=a[0];
for aa in a:
    if aa<max:
        sum=sum+max-aa
    else:
        max=aa

print(sum)