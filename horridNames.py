import random
first = ['craig','phil','ayd','bryn','rya','jova','zae','avi','jace','ade','kay','bray','paiz','kayt','jayce','kam']
last = ['lyn','lynn','elle','ory','liper','lee','zlee','ree','leigh','leaigh','den','don','son','syn','myn','nee','ryn']
def makename():
	newname = random.choice(first) + random.choice(last)
	print(newname)
	def runtime():
		doOver=str.lower(input('Make another horrible name? Y/N\n'))
		if doOver == 'y' or doOver == 'yes':
			makename()
		else:
			pass
	runtime()
makename()
