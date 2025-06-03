if __name__ == "__main__":
    nums =map( int, raw_input().split())
    if nums[0] < nums[1]:
        if nums[1] < nums[2]:
            print "Yes"
        else:
            print "No"
    else:
        print "No"