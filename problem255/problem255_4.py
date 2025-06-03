n = input()
s = list(map(str, input().split()))
news = ""
for i in range(int(n)):
    news += s[0][i] + s[1][i]
print(news)