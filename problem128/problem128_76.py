x, num_of_nums = map(int, input().split(' '))

if num_of_nums == 0:
    print(x)
    exit()
    
nums = set(map(int, input().split(' ')))

diff = 0

while True:
    n1 = x - diff
    n2 = x + diff

    if n1 not in nums:
        print(n1)
        break
    
    if n2 not in nums:
        print(n2)
        break
    
    diff += 1