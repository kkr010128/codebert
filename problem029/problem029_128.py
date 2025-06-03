values=input().split()
x1=float(values[0])
y1=float(values[1])
x2=float(values[2])
y2=float(values[3])
x_distance=x2-x1
y_distance=y2-y1
print(pow(pow(x_distance,2)+pow(y_distance,2),0.5))
