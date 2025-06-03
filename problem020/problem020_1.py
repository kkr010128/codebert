A=[]
fp =0
bp =0
 
n=int(raw_input())
while n:
    s = raw_input()
    if s[0] == 'i':
        A.append(int(s[7:]))
        fp += 1
    elif s[6] == ' ':
        try:
            i = A[::-1].index(int(s[7:]))
            if i!=-1:
                del A[-i-1]
                fp -=1
        except:
            pass
    elif s[6] == 'F':
        A.pop()
        fp -=1
    elif s[6] == 'L':
        bp +=1
    n -=1
 
for e in A[bp:fp+1][::-1]:
    print int(e),