a,b,c,d = map(int,input().split())
x_1,x_2,y_1,y_2 = (a*c,a*d,b*c,b*d)
num_list = [x_1,x_2,y_1,y_2]
print(max(num_list))