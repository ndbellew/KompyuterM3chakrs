def splitinput(line):
	for x in line.split():
		yield int(x)
		

def main():
	n = int(input())
	out = []
	for i in range(n):
		line = input()
		r, e, c = splitinput(line)
		if (r+c)<e:
			out.append("advertise")
		elif (r+c)>e:
			out.append("do not advertise")
		else:
			out.append("does not matter")
	for i in out:
		print(i)


if __name__ == "__main__":
	main()