import math
gun_list = [1]
for i in range(11):
    gun_list.append(gun_list[-1]+26**(i+1))
#print(gun_list)
#郡の始まりのnumをしまったリスト
a =int(input())
#print()
gun_sum = 12
for i in range(13):
    if gun_list[i] <= a and gun_list[i+1] > a:
        gun_num = i
        break
#print(gun_num)
b = a-gun_list[gun_num]
#print(b)

x_list = [26**i for i in range(gun_num+1)]
x_list = x_list[::-1]
#print(x_list)

ans_list = []
for i in range(len(x_list)):
    if i > 0:
        b -= x_list[i-1]*ans_list[i-1]
        
        ans_list.append(math.floor(b/x_list[i]))
    else:
        ans_list.append(math.floor(b/x_list[0]))
    

#print(ans_list)

ans = ''
for i in range(len(ans_list)):
    ans += chr(97+ans_list[i])
    #print(ans)
print(ans)