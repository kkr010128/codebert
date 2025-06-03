S = int(input())
sum_all = 0
sum_fizzbuzz = 0
for i in range(1,S+1):
    sum_all = sum_all + i
    if i % 3 == 0 or i % 5 == 0 or i % 15 ==0:
        sum_fizzbuzz = sum_fizzbuzz + i
#print(sum_all)
#print(sum_fizzbuzz)
print(sum_all - sum_fizzbuzz)