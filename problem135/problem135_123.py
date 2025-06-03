A,B= list(input().split())
a = int(B[0])
b = int(B[2])
c = int(B[3])
if int(A) > 1000:
   e = int(A[-2])
   f = int(A[-1])
   d = int((int(A)- 10 * e - f)/100)
   error = 10 * (c * e + b * f) + c * f
   error = int(error/100)
   ans = int(A) * a + 10 * d * b + e * b + c * d + error
   print(int(ans))
else:
   print(int(int(A)*float(B)))