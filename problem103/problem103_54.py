n = int(input())
a = list(map(int,input().split()))
b = [0]*n
for i in range(n-1):
    if(a[i] < a[i+1]):
        #if(b[i-1] < 1):
        b[i] = 1
        #else:
        #    b[i] = 2
    if(a[i] > a[i+1]):
        #if(b[i-1] > -1):
        b[i] = -1
        #else:
        #    b[i] = -2
    #else:
        #if(b[i-1] > 0):
    #       b[i] = 2
     #   else:
      #      b[i] = -2
b[-1] = -1
#print(b)
h = [1000,0]
for i in range(n):
    if(b[i] == 1):
        h[1] += h[0]//a[i]
        h[0] %= a[i]
    elif(b[i] == -1):
        h[0] += h[1]*a[i]
        h[1] *= 0
    #print(h)
print(h[0])