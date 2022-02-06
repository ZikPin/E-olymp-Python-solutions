def solver(days):
	month = [0 for i in range(31)]
	for i in days:
		for k in range(i[0]-1, i[1]):
			month[k] += 1
	if max(month) == len(days):
		return "YES"
	else:
		return "NO"

test = int(input())
while test>0:
	n = int(input())
	days = []
	while n>0:
		days.append(list(map(int, input().split())))
		n -= 1
	print(solver(days))
	test -= 1
