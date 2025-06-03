# coding: utf-8

import math

n = int(raw_input())

def vector_rot(vector, radian):
	new_x = vector[0] * math.cos(radian) - vector[1] * math.sin(radian)
	new_y = vector[0] * math.sin(radian) + vector[1] * math.cos(radian)
	return [new_x, new_y]

def vector_add(v1, v2):
	new_v = []
	for i in range(2):
		add = v1[i] + v2[i]
		new_v.append(add)
	return new_v

def makepoint(p_A1, p_A2):
	x_p_C1 = (p_A2[0] - p_A1[0]) / 3 + p_A1[0]
	y_p_C1 = (p_A2[1] - p_A1[1]) / 3 + p_A1[1]
	x_p_C3 = (p_A2[0] - p_A1[0]) * 2 / 3 + p_A1[0]
	y_p_C3 = (p_A2[1] - p_A1[1]) * 2 / 3 + p_A1[1]

	p_C1 = [x_p_C1, y_p_C1]
	p_C3 = [x_p_C3, y_p_C3]

	v01 = [x_p_C1 - p_A1[0], y_p_C1 - p_A1[1]]
	rot_v01 = vector_rot(v01, 60 * math.pi / 180)
	v02 = vector_add(v01, rot_v01)
	p_C2 = vector_add(p_A1, v02)	
	
	C = [p_C1, p_C2, p_C3]
	return C

A = [[0., 0.],[100., 0.]]
for i in range(n):
	B = []
	for j in range(len(A)-1): #A[j]??¨A[j+1]
		C = makepoint(A[j], A[j+1]) #C = [p_C1, p_C2, p_C3]
		B.append(A[j])
		for p in C:
			B.append(p)
		#A[j+1]????¬????makepoint?????????append??????
	B.append(A[-1]) #??????????????\?????\??????
	A = B

for x in A:
	print("{:.8f}".format(x[0])),
	print("{:.8f}".format(x[1]))