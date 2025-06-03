n, m = map(int, input().split())
number = [0] * n
cou = [0] * n
#logging.debug(number)#

for i in range(m):
    s, c = map(int, input().split())
    s -= 1
    if cou[s] > 0 and c != number[s]:
        print(-1)
        exit()
    else:
        cou[s] += 1
        number[s] = c
    #logging.debug("number = {}, cou = {}".format(number, cou))

if n > 1 and number[0] == 0 and cou[0] >= 1:
    print(-1)
    exit()
elif n > 1 and number[0] == 0:
    number[0] = 1

number = map(str, number)
print(''.join(number))