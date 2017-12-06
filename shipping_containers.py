import math
height= 8.5
length= 20
width= 8

def how_many_containers():
	get_height = float(input("enter height of structure in feet\n"))
	get_length = float(input("enter length of structure in feet\n"))
	get_width = float(input("enter width of structure in feet\n"))
	height_needs = round((get_height / height),2)
	length_needs = round((get_length / length),2)
	width_needs = round((get_width / width),2)
	measures_list = [height_needs,length_needs,width_needs]
	max_containers = math.ceil(float(max(measures_list)))
	print("Your structure is {} standard 20' shipping containers tall, {} containers long, and {} containers wide. You will need at least {} standard 20' shipping containers. Neato!".format(height_needs,length_needs,width_needs,max_containers))

how_many_containers()
