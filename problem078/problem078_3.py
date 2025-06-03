n = int(input())
all = 10**n
all -= 9**n*2-8**n
print(all%(10**9+7))    
