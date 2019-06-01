import random
length = 0
def measure():
        global length
        widthrange = []
        for i in range(8, 51):
                widthrange.append(i)
        width= random.choice(widthrange)
        lengthrange = []
        for i in range(8,51):
                lengthrange.append(i)
        def lengthpicker():
                global length
                lenTry = random.choice(lengthrange)
                if 18 <= (lenTry + width) <= 50:
                        length = lenTry
                else:
                        lengthpicker()
        lengthpicker()
        sqft = length*width
        print("Length is {} feet. Width is {} feet. Total square footage is {}.".format(length,width,sqft))

measure()

