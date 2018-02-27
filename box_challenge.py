#boxes coding challenge
#sort boxes into three even stacks
from itertools import permutations


info = raw_input(str("enter inputs here"))
stacks, total = info.split(" ")
stacks = int(stacks)
boxes = [int(x) for x in total]
boxes.sort()
height = sum(boxes)/stacks
correct_subset = []

#check if possible first
def check(boxes, stacks):
	if sum(boxes)%(stacks) != 0:
		print("not possible to stack evenly")
	elif boxes[-1] > height:
		print("One or more stacks are too tall")
	else:
		print("Good to go! Proceeding to calculate")
		
#sort it into groups		
def sort(boxes, stacks):
	global correct_subset
	correct_subset = [] 
	for i in boxes:
		if i == height:
			correct_subset.append(i)
			print(correct_subset)  #once this happens all the rest will since not too tall and sorted
		else:
			n = len(boxes)
			for j in boxes[boxes.index(i)+1:n]:
				while group = sum(i + j) 
				if group == height:
					correct_subset.append(i,j)
					print(correct_subset)
				else:



# check for repeats
	





