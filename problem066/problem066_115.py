while True:
    first_string=input()
    if first_string=="-":
        break
    lst=list(first_string)
    m=int(input())
    for i in range(m):
        h=int(input())
        for l in range(1,h+1):
            letter=lst.pop(0)
            lst.insert(len(lst),letter)
    answer_string=''
    for m in lst:
        answer_string+=m
    print(answer_string)
