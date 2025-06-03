n,k = map(int,input().split())

p = [int(x) for x in input().split()]

sum1 = sum(p[:k])
num = k-1
max1 = sum1

for i in range(k,n):
    sum1 = sum1 - p[i-k] + p[i]
    if sum1 >= max1:
        max1 = sum1
        num = i
    #print(max1,sum1,i)

sum2 = sum(p[num-k+1:num+1])

def goukei(j):
    return 1/2 * j * (j+1)

print(float((goukei(sum2)-goukei(k-1))/(sum2 -k +1)))
