n = int(input())

sumall = int(n * (n+1)/2)
sum3 = int(n//3 * (n//3 + 1) * 3/2)
sum5 = int(n//5 * (n//5 + 1) * 5/2)
sum15 = int(n//15 * (n//15 + 1) * 15/2)

print(sumall - sum3 - sum5 + sum15)