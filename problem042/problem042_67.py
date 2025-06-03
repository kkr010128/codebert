counter = 1
while True:
    x = int(input())
    if x == 0:
        break
    else:
        print('Case', '{}{}{}'.format(counter, ': ', x))
        counter += 1
 