def main():                                                                     
  n = int(raw_input())                                                          
  data = {}                                                                     
                                                                                
  for a in xrange(1,n):                                                         
      b = n-a                                                                   
      if a == b:                                                                
          continue                                                              
      data[(min(a,b), max(a, b))] = 1                                           
                                                                                
  print(len(data.keys()))                                                       
                                                                                
main()