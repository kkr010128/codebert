a = int(input())
b = int(input())
 
t = set([1, 2, 3])
s = set([a,b])
ans = t - s
print(list(ans)[0])