user_input=input()
i=len(user_input)-1
number=0
while i>=0:
        number+=int(user_input[i])
        i=i-1
if number%9==0:
    print("Yes")
else :
    print("No")
