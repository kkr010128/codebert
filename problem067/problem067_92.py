round=int(input())
T_pt=0
H_pt=0

for i in range(round):
	pair=raw_input().split(" ")
	T_card=pair[0].lower()
	H_card=pair[1].lower()

	if T_card<H_card:
		H_pt+=3
	elif T_card>H_card:
		T_pt+=3
	else:
		T_pt+=1
		H_pt+=1
print T_pt,H_pt