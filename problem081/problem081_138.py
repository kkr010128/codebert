#輸入字串並分隔，以list儲存
str_in = input()
num = [int(n) for n in str_in.split()]
num =list(map(int, str_in.strip().split()))  
#print(num) #D,T,S

#若T<(D/S)->遲到
if num[1] >= (num[0]/num[2]):
    print("Yes")
else:
    print("No")


