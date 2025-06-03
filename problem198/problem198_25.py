n = int(input())
dict = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j"}
dict2 = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
#ans = [["a", 1]]
#for i in range(n-1):
#    newans = []
#    for lis in ans:
#        now = lis[0]
#        count = lis[1]
#        for j in range(1, count + 2):
#            newans.append([now + dict[j], max(j, count)])
#    ans = newans
#for lis in ans:
#    print(lis[0])
def dfs(s):
    if len(s) == n:
        print(s)
        return
    m = max(s)
    count = dict2[m]
    for i in range(1, count+2):
        dfs(s+dict[i])
dfs("a")