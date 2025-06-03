input()
X_vec = map(float, input().split())
Y_vec = map(float, input().split())
pair = list(zip(X_vec, Y_vec))
D1 = sum(abs(x-y) for x,y in pair)
D2 = (sum((x-y)**2 for x,y in pair)) ** .5
D3 = (sum(abs(x-y)**3 for x,y in pair)) ** (1/3)
Dinf = max(abs(x-y) for x,y in pair)
print("{0:.6f}\n{1:.6f}\n{2:.6f}\n{3:.6f}\n".format(D1,D2,D3,Dinf))