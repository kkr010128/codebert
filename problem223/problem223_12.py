n, k = map(int, input().split())
p = list(map(int, input().split()))

#logging.debug("デバッグスタート") #
l = [[] for i in range(n)]#期待値
m = [[] for i in range(n - k + 1)]  #k個の合計

for i in range(n):
    l[i] = (1 + p[i]) / 2

#logging.debug("l = {}".format(l))#
m[0] = sum(l[0:k])
ans = m[0]

for i in range(1, n - k + 1):
    #logging.debug("m[i-1] = {} ,l[i-1] = {} ,l[i+k] = {}".format(m[i - 1], l[i - 1], l[i + k - 1]))  #
    m[i] = m[i - 1] - l[i - 1] + l[i + k - 1]
    if m[i] > ans:
        ans = m[i]

#logging.debug(m)#
print(ans)