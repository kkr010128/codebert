l=raw_input()
k=l.split()
a=int(k[0])
op=k[1]
b=int(k[2])
#
while op<>'?':
        if op=='+':
                print a + b
        if op=='-':
                print a - b
        if op=='*':
                print a * b
        if op=='/':
                print a / b
#
        l=raw_input()
        k=l.split()
        a=int(k[0])
        op=k[1]
        b=int(k[2])