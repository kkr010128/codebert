str = input()
 
str_length = len(str)
 
import random
 
start_num = random.randint(0,str_length-3)
 
print(str[start_num:start_num+3])
