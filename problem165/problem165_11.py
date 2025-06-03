n = int(input());

dict = {}

for i in range(n):
    s = input();
    if not s in dict:
        dict[s] = 1

sum = 0
for i in dict:
    sum += 1

print(sum)
