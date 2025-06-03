# coding: utf-8
# Your code here!
def multiple_3(num):
    if num % 3 == 0:
        print(" {}".format(num), end="")
    else:
        included_3(num)

def included_3(num):
    if "3" in str(num):
        print(" {}".format(num), end="")
        
n = int(input())
for num in range(3, n+1):
    multiple_3(num)
print()

