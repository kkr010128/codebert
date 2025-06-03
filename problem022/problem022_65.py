n = raw_input()                                                
l = map(int, raw_input().split())                              
n = raw_input()                                                
                                                               
sum = 0                                                        
for i in map(int, raw_input().split()):                        
    if i in l:                                                 
        sum += 1                                               
                                                               
print sum