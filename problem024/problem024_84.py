import sys

def binarySearch(t,w):
    left = max(w)
    right = sum(w)
    while left < right:
        middle = (left + right) // 2
        if hantei(t,w,middle):
            right = middle 
        else:
            left = middle + 1
    return left
            
def hantei(t,w,p):
    track_on = 0
    daisu = 1
    for j in range(len(w)):     
        track_on += w[j]
        if track_on > p:
            daisu += 1
            track_on = w[j]
            if daisu > t:
                return False
    return True


nimotsu, track = map(int,input().split())
weight = list(map(int,sys.stdin.readlines()))



print(binarySearch(track,weight))