from collections import Counter
ABC = list(map(int, input().split()))
ABC = Counter(ABC)
if len(ABC) == 2:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
