def merge_sort(A):
    if len(A) <= 1:
        return A, 0
    mid = len(A) // 2
    left, lcount = merge_sort(A[:mid])
    right, rcount = merge_sort(A[mid:])
    merged, count = merge(left, right)
    return merged, lcount + rcount + count

def merge(left, right):
    lpos = 0
    rpos = 0
    #lcount = 0
    #rcount = 0
    merged = []
    while lpos < len(left) and rpos < len(right):
        if left[lpos] <= right[rpos]:
            merged.append(left[lpos])
            lpos += 1
            #lcount += 1
        else:
            merged.append(right[rpos])
            rpos += 1
            #rcount += 1
    
    if left[lpos:]:
        merged.extend(left[lpos:])
        #lcount += len(left[lpos:])
    if right[rpos:]:
        merged.extend(right[rpos:])
        #rcount += len(right[rpos:])
    
    #print merged
    #return merged, lcount + rcount
    return merged, len(merged)

if __name__ == '__main__':
    n = int(raw_input())
    A = map(long, raw_input().split())
    
    sorted, count = merge_sort(A)
    print ' '.join(str(x) for x in sorted)
    print count