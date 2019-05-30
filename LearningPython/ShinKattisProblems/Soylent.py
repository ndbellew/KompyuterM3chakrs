import math
def main():
	n = int(input())
	out = []
	for i in range(n):
		cal = int(input())
		cal = math.ceil(cal/400)
		out.append(cal)
	for i in out:
		print(i)


if __name__ == "__main__":
	main()