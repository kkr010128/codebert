IDX_TABLE=\
{1:[4,2,3,5],
 2:[1,4,6,3],
 3:[1,2,6,5],
 4:[1,5,6,2],
 5:[4,1,3,6],
 6:[3,2,4,5]}

nums = ["dummy"] + [int(x) for x in raw_input().split(" ")]
n = int(raw_input())

for i in range(n):
    up, front = tuple([int(x) for x in raw_input().split(" ")])
    up_idx = nums.index(up)
    front_idx = nums.index(front)
    ring_list = IDX_TABLE[up_idx]
    ring_idx = ring_list.index(front_idx)

    print nums[ring_list[(ring_idx+1) % 4]]