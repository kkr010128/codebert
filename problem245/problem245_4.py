n = int(input())
X = input()
a = 0
for i in range(n-2):
  if X[i] + X[i+1] + X[i+2] == 'ABC':
    a +=1
  else:
    a +=0
      
print(a)