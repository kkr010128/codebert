a,b,c,d = map(int,input().split(' '))
matrix = []
matrix.append(a*c) 
matrix.append(a*d) 
matrix.append(b*d) 
matrix.append(b*c) 

matrix = sorted(matrix, reverse=True)

print(str(matrix[0]))