n=int(input())
p=10**9+7
total=(10**n)%p
except_0=(9**n)%p
except_9=except_0
except_both=(8**n)%p
# double reduced from [1,8]
# so add that
print((total-except_0-except_9+except_both)%p)