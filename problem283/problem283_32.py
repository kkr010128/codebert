num = int(input())

# if num % 2 == 0:
#     half = num / 2
# else:
#     half = int(num  + 1) / 2

half = int(num / 2)

count = 0

for i in range(1, half + 1):
    a = i
    b = num - i
#     print(a,b)
    if a != b:
        count += 1
    
print(count)