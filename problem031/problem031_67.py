import statistics as st

while(1):
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    print(st.pstdev(s))