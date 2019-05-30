
def main():
	x = int(input())
	for i in range(x):
		nm = input().split()
		m = int(nm[1])
		n = int(nm[0])
		subarray = input().split()
		for i in range(len(subarray)):
			subarray[i] = int(subarray[i])
	sumL = []
	sum = 0
	maxsum = 0
	for i in range(n):
		if i >=2:
			repeat = 0
			sub = [subarray[i],subarray[i-1],subarray[i-2]]
			for i in sub:
				if i == m:
					repeat+=1
				if i <m:
					repeat+=2
			sum = sub[0]+sub[2]+sub[1]
			if sum>maxsum and repeat ==1:
				maxsum = sum
	sumL.append(maxsum)

	for i in sumL:
		print(i)

if __name__=="__main__":
	main()
	"""
	run through the list and allow for the checker to see if the minimum shows up if anything less then the minimum shows up, add the chunk up that point, get the sum, and then make that the maxsum
	after that restart sublist starting after the number less than the minimum or start on the second minimum and go again until findint a number less than or equal to the minimum not including that number
	add them up and check the max num, when you reach the end of the list, print the maxnum
	"""
