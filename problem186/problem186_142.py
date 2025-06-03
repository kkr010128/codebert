k,n=map(int,input().split())
a=[int(i)for i in input().split()]
distance=[a[i+1]-a[i] for i in range(n-1)]
distance.append(a[0]+k-a[-1])
print(sum(distance)-max(distance))