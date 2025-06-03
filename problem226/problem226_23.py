str = input()
str2 = input()
nums  = str.split()
nums2  = str2.split()
if len(nums2) != int(nums[1]):
    print("error")
else:
   totalDamege = 0
   for num in nums2:
       totalDamege += int(num)
   if int(nums[0]) <= totalDamege:
       print("Yes")
   else:
       print("No")
