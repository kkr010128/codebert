x = list(map(int, input().split()))
x0 = [x[0], x[1]]
y0 = [x[2], x[3]]
results = [(x0[0]*y0[0]), (x0[1]*y0[0]), (x0[0]*y0[1]), (x0[1]*y0[1])]
print(max(results))