import statistics as st
while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    print(f'{st.pstdev(s):.5f}')
