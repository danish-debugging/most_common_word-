num = int(input('Enter max limit till you wanna recieve odd numbers: '))
li = list()
li=[i*i for i in range(1,num+1) if i%2!=0]
print(li)
