
if __name__ == "__main__":
    nums = map( int, raw_input().split())
    nlen = len( nums )
    nlast = nlen - 1
    while 0 < nlast:
        j = 0
        while j < nlast:
            if nums[j] > nums[j+1] :
                d = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = d
            j += 1
        nlast -= 1

    nlast = nlen - 1
    i = 0
    while i < nlen:
        if i != nlast:
            print nums[i],
        else:
           print nums[i]
        i += 1