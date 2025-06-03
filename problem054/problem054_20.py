n = int(input())
lst = [(m,no) for m in ['S','H','C','D'] for no in range(1,14)]
for i in range(n):
    m,no = input().split()
    lst.remove((m,int(no)))
for (m,no) in lst:
    print(m,no)
