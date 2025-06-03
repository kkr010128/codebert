N = int(input())
a = map(int, input().split())

even = [i for i in a if i % 2 == 0]
for check in even:
  if check % 3 != 0 and check % 5 != 0:
    print('DENIED')
    exit()
print('APPROVED')