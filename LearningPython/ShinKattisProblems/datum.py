def DayOfWeek(D,M):
	days=D
	if M != 1:
		for i in range(1, M):
			if i == 2:
				days += 28
			elif i == 8 or i ==10 or i ==12:
				days += 31
			elif i%2 == 0 or i ==9 or i == 11:
				days += 30
			else:
				days += 31
	return days%7
def main():
	D, M = input().split()
	D = int(D)
	M = int(M)
	dic = {0:"Wednesday", 1:"Thursday", 2:"Friday", 3:"Saturday", 4:"Sunday", 5:"Monday", 6:"Tuesday"}
	print(dic[DayOfWeek(D, M)])

if __name__ == "__main__":
	main()
