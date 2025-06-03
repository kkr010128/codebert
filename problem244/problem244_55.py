import os

def main():
	k, x = map(int, input().split())
	if x <= 500 * k:
		print("Yes")
	else:
		print("No") 

if __name__ == '__main__':
	main()

