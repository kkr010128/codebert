S = int(input())

for i in range(9) :
    i = i + 1
           
    if S % i == 0 and S // i <= 9:
        result = "Yes"
        break
    else :
        result = "No"
print(result)
