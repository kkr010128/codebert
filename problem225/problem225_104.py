import math

hp, attack = map(int, input().split())

print(math.ceil(hp / attack))

# x, y = divmod(hp, attack)
#
# if y == 0:
#     print(x)
# else:
#     print(x + 1)

# count = 0
# 
# while True:
#     hp -= attack
#     count += 1
# 
#     if hp <= 0:
#         print(count)
#         break
# 
