inputValues = [int(i) for i in input().split()]
n = inputValues[0]
k = inputValues[1]
res = n%k
res = min(k-res,res)
print(res)
