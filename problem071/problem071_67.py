word = list(input())
if word[-1] == "s":
    word.append("es")
    ans = "".join(word)
else:
    word.append("s")
    ans = "".join(word)
print(ans)