total=0
while True:
	num = input('Enter your statement for D or W: ')
	try:
		statement = num.split(' ')
		value = int(statement[1])
		if statement[0]=='D':
			total = total + value
		elif statement[0]=='W':
			total = total - value
		if statement[0]=='done':
			break
	except :
		print(f'total sum for your statement is {total}')
		quit()
print(f'total sum for your statement is {total}')