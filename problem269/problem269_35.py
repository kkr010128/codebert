t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

sum_a = t1 * a1 + t2 * a2
sum_b = t1 * b1 + t2 * b2

if sum_a == sum_b:
    print('infinity')
    exit()
    
if sum_a > sum_b:
    big_sum = sum_a
    big_1 = a1*t1
    big_2 = a2*t2
    sml_sum = sum_b
    sml_1 = b1*t1
    sml_2 = b2*t2
else:
    big_sum = sum_b
    big_1 = b1*t1
    big_2 = b2*t2
    sml_sum = sum_a
    sml_1 = a1*t1
    sml_2 = a2*t2
    
if sml_1 < big_1:
    print(0)
    exit()
    
#print(big_sum,sml_sum)
    
n = (big_1-sml_1) // (sml_sum-big_sum)

if (big_1-sml_1) % (sml_sum-big_sum) == 0:
    print(n*2)
else:
    print(n*2+1)
