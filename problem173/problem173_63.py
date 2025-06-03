n = int(input())
a = []
lists = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        a.append('FizzBuzz')
    elif i % 3 == 0:
        a.append('Fizz')
    elif i % 5 == 0:
        a.append('Buzz')
    else:
        a.append(str(i))

for item in a:
    item = item.replace('FizzBuzz', '0')
    item = item.replace('Fizz', '0')
    item = item.replace('Buzz', '0')
    lists.append(item)

print(sum([int(i) for i in lists]))
