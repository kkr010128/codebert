def bubble_sort(List):
	cnt=0
	l=len(List)
	for i in range(l):
		for j in range(l-1,i,-1):
			if List[j]<List[j-1]:
				temp=List[j]
				List[j]=List[j-1]
				List[j-1]=temp
				cnt+=1
	return cnt
def main():
	N=input()
	N_List=map(int,raw_input().split())
	cnt=bubble_sort(N_List)
	for k in range(len(N_List)):
		N_List[k]=str(N_List[k])
	print(" ".join(N_List))
	print(cnt)

if __name__=='__main__':
	main()