num=int(raw_input().strip())

lst=map(int,raw_input().strip().split())
def sort(lst,idx):
    tmp=lst[idx]
    idx-=1
    while idx>=0 and lst[idx]>tmp:
        lst[idx+1]=lst[idx]
        idx-=1
    lst[idx+1]=tmp

for ii in xrange(num):
    sort(lst,ii)
    print " ".join(str(i) for i in lst)
