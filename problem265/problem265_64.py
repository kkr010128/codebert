n = int(input())
import math
a = n*100/108
b = (n*100+100)/108
ans = math.ceil(a) if math.ceil(a) < b else ":("
print(ans)