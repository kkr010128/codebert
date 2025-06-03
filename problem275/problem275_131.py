X, Y = map(int, input().split())
print(400000*(X==1)*(Y==1) + max(0, 400000-100000*X) + max(0, 400000-100000*Y))