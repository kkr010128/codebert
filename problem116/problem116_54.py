first_string = input()
second_string = input()
count = 0

for x, y in zip(first_string, range(len(first_string))):
    if(second_string[y] != x):
        count += 1
print(count)