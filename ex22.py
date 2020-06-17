s = input('Enter your statement please!! ')
statement = s.split(' ')
dic=dict()
for words in statement:
	dic[words] = dic.get(words,0)+1
print(dic)
square_dict=dict()
def squareofkeys():
	for i in range(1,4):
		square_dict[i]=i*i
	print(square_dict.keys())
print(squareofkeys())

def squarelist():
	li = [i**i for i in range(1,21)]
	print(li)
	x=tuple(li)
	print(x)

squarelist()

exampletuple = (1,2,3,4,5,6,7,8,9,10)
print(exampletuple[:5])
print(exampletuple[5:])

li1 = [1,2,3,4,5,6,7,8,9,10]
even_li1 = map(lambda i:i**i, filter(lamda i:i%2==0),li1)
print(even_li1)

