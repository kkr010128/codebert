str = input()
nums  = str.split()
if nums[0] == "0" or nums[1] == "0":
     print("error")
else:
    turn = float(nums[0]) / float(nums[1]) + 0.9
    if turn < 1:
       turn = 1
    print(int(turn))