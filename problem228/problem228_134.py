#a(n) = 2^ceiling(log_2(n+1))-1
import math
print(2**(math.ceil(math.log2(int(input())+1)))-1)