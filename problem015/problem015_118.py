def insection_sort(lst):
    lens=len(lst)
    ans=0
    for i in xrange(lens):
        mn=i
        for j in xrange(i+1,lens):
            if(lst[j]<lst[mn]):
                mn=j
        if(mn!=i):
            tmp=lst[i]
            lst[i]=lst[mn]
            lst[mn]=tmp
            ans+=1
    return ans
num=int(raw_input().strip())
arr=map(int,raw_input().strip().split())
ans=insection_sort(arr)
print " ".join(str(pp) for pp in arr)
print ans

