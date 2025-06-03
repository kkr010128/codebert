n,m,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

def make_sumlist(book_list):
    sumnum=0
    container=[0]
    for i in book_list:
        container.append(sumnum+i)
        sumnum+=i
    return container

total_a=make_sumlist(a)
total_b=make_sumlist(b)

# print(n,m,k)
# print(total_a)
# print(total_b)


#r個読めるか
def readable(r):
    #全部読んでも無理
    if r>n+m:
        return False
    if r==0:
        return True
    max_book=100000000000
    for a_n in range(max(0,r-m),min(n,r)+1):
        b_n=r-a_n
        # print(a_n,b_n)
        book_sum=total_a[a_n]+total_b[b_n]
        # print(book_sum)
        max_book=min(max_book,book_sum)
    if max_book<=k:
        return True
    return False

def nibuntansaku(start,end):
    if start==end:
        return start
    middle=(start+end)//2+1
    if readable(middle):
        start=middle
    else:
        end=middle-1
    return nibuntansaku(start,end)

print(nibuntansaku(0,k))
