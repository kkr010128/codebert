while True:                                  
  m, f, r = [int(_) for _ in input().split()]
  if m == -1 and f == -1 and r == -1:        
    break                                    
  sum = m+f                                  
  if m == -1 or f == -1 or sum < 30:         
    print("F")                               
  else:                                      
    if sum >= 80:                            
      print("A")                             
    elif sum >= 65:                          
      print("B")                             
    elif sum >= 50:                          
      print("C")                             
    else:                                    
      if r >= 50:                            
        print("C")                           
      else:                                  
        print("D")                           