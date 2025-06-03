import math
import cmath
def check(inp):
    if inp==2:
        return True
    for num in xrange(2,int(math.sqrt(inp)+1)):
        if inp%num==0:
            return False
    return True
st=set()


while True:
    try:
       str=raw_input().strip()

    except EOFError:
        break
    #print str
    num=int(str)
    st.add(num)
sum=0
for nm in st:
    if check(nm):
        sum+=1
print sum
