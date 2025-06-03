n = input()
ans = ""
for i in range(1, n + 1) :
    if (i % 3 == 0 or str(i).count('3')) :
        ans += (" " + str(i))
print("%s" % ans)