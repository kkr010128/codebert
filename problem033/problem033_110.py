#N E S W
def move_func(dice_list, dir):
	new_dice = []
	if dir=="N":
		new_dice.append(dice_list[1])
		new_dice.append(dice_list[5])
		new_dice.append(dice_list[2])
		new_dice.append(dice_list[3])
		new_dice.append(dice_list[0])
		new_dice.append(dice_list[4])
	elif dir=="E":
		new_dice.append(dice_list[3])
		new_dice.append(dice_list[1])
		new_dice.append(dice_list[0])
		new_dice.append(dice_list[5])
		new_dice.append(dice_list[4])
		new_dice.append(dice_list[2])
	elif dir=="S":
		new_dice.append(dice_list[4])
		new_dice.append(dice_list[0])
		new_dice.append(dice_list[2])
		new_dice.append(dice_list[3])
		new_dice.append(dice_list[5])
		new_dice.append(dice_list[1])
	elif dir=="W":
		new_dice.append(dice_list[2])
		new_dice.append(dice_list[1])
		new_dice.append(dice_list[5])
		new_dice.append(dice_list[0])
		new_dice.append(dice_list[4])
		new_dice.append(dice_list[3])
	return new_dice

try:
	while True:
		dice_list = input().split(" ")
		move_cmd = input()
		for cmd in  move_cmd:
			dice_list = move_func(dice_list, cmd)
			
		print(dice_list[0])
except EOFError:
	pass