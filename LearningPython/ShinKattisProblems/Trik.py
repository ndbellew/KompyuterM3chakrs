
def main():
	position = 1
	move = input()
	for i in range(len(move)):
		if position == 1:
			if move[i] == 'A':
				position = 2
			elif move[i] == 'C':
				position = 3
		elif position == 2:
			if move[i] == "A":
				position = 1
			elif move[i] == "B":
				position = 3
		else:
			if move[i] == 'B':
				position = 2
			elif move[i] == 'C':
				position = 1
	print(position)
	
if __name__ == "__main__":
	main()