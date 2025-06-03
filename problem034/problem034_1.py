import copy

class Dice(object):
	def __init__(self,List):
		self.face=List
		
	def n_spin(self,a_list):
		List=copy.copy(a_list)
		temp=List[0]
		List[0]=List[1]
		List[1]=List[5]
		List[5]=List[4]
		List[4]=temp
		return List
		
 	def s_spin(self,a_list):
 		List=copy.copy(a_list)
 		temp=List[0]
 		List[0]=List[4]
 		List[4]=List[5]
		List[5]=List[1]
		List[1]=temp
		return List
		
	def e_spin(self,a_list):
		List=copy.copy(a_list)
		temp=List[0]
		List[0]=List[3]
		List[3]=List[5]
		List[5]=List[2]
		List[2]=temp
		return List
		
 	def w_spin(self,a_list):
 		List = copy.copy(a_list)
 		temp=List[0]
 		List[0]=List[2]
 		List[2]=List[5]
		List[5]=List[3]
		List[3]=temp
		return List

dice=Dice(map(int,raw_input().split()))
emer=copy.copy(dice.face)
face_storage=[]
face_storage.append(emer)
q=input()
for a in range(q):
	question=map(int,raw_input().split())
	for a in range(24):
		face_storage.append(dice.n_spin(face_storage[a]))
		face_storage.append(dice.s_spin(face_storage[a]))
		face_storage.append(dice.e_spin(face_storage[a]))
		face_storage.append(dice.w_spin(face_storage[a]))
	for c in face_storage:
		if c[0]==question[0] and c[1]==question[1]:
			print(c[2])
			break