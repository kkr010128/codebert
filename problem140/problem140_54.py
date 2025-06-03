s = input()
#print(s.replace("?", "D"))


ans = []
for i in s:
    if i == "P":
        ans.append("P")
    else:
        ans.append("D")
print("".join(ans))
