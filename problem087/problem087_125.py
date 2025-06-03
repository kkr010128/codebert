'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

ip=list(input())
sum=0
for i in ip:
    sum+=int(i)
if sum%9==0:
    print('Yes')
else:
    print('No')