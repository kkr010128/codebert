a,b = map(int,input().split())
word = ""
for i in range(max(a,b)):
    word += str(min(a,b))
print(word)

