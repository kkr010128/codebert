import sys                                                
n = int(sys.stdin.readline())                             
                                                          
xs = []                                                   
for _ in range(n):                                        
  v = [int(x) for x in sys.stdin.readline().split(" ")]   
  xs.append(v)                                            
                                                          
xs.sort(key=lambda x: x[0])                               
if n % 2 == 0:                                            
  m1 = n // 2 - 1                                         
  m2 = m1 + 1                                             
  a1 = xs[m1][0]                                          
  a2 = xs[m2][0]                                          
  xs.sort(key=lambda x: x[1])                             
  b1 = xs[m1][1]                                          
  b2 = xs[m2][1]                                          
  a = (a1 + a2)                                           
  b = (b1 + b2)                                           
  c = (b - a) + 1                                         
  #print(m1, m2, a1, a2, b1, b2, "*", a, b, c)            
  print(c)                                                
else:                                                     
  m = (n + 1) // 2 - 1                                    
  a = xs[m][0]                                            
  xs.sort(key=lambda x: x[1])                             
  b = xs[m][1]                                            
  c = b - a + 1                                           
  #print(m, a, b, c)                                      
  print(c)                                                