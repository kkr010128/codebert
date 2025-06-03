n = int(input())


if n%2 == 1:
    print(0)
else:
    answer = 0
    count = 1
    n=n//2
    while 5**count <= n:
        answer += n//pow(5,count)
        count+=1
    print(answer)