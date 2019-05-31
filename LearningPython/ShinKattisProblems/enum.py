def factorial(num):
	if num == 0:
		return 1
	fact = 1
	for i in range(1, num+1):
		fact = fact * i
	return fact

def main():
	n = int(input())
	out = 1
	temp = 0
	for i in range(1, n+1):
		out += 1/factorial(i)
		if out == temp:
			break
		temp = out
	print (out)
	
if __name__ == "__main__":
	main()