k = int(input())
s = input()
lists = list(s)
news = list()
if len(lists) <= k:
    print(s)
else:
    for i in range(k):
        news.append(lists[i])
    result = "".join(news)
    print(result + "...")