M =  10**9 + 7 
n = int(input())
a = [int(i) for i in input().split()]  #; print(a)

counter = [0] * (n+1) ; counter[0] = 3
ans = 1
for i in range(n):
    ans *=  counter[a[i] - 1 +1] - counter[a[i] +1]
    ans = ans % M
    counter[a[i] +1] += 1
print(ans)