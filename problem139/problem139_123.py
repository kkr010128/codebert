line_data = input()                                               
H1, M1, H2, M2, K = map(lambda x: int(x), line_data.split(' '))   
                                                                  
miniutes = (H2 - H1) * 60 + (M2 - M1)                             
                                                                  
print(miniutes - K)                                               
