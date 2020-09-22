# takes a unsorted list and sorts it in assending values
# does this by comparing two values at a time, the lower of the two values will get moved to the left with the higher of the two remaining on the right
# the function will continue to sort through the list sorting the highest value to the right untill the highest value is on the right a 'break' is called

def bubble(list_a):
	indexing_length = len(list_a) - 1
	sorted = False

	while not sorted:
		sorted = True
		for i in range(0, indexing_length):
			if list_a[i] > list_a[i+1]:
				sorted = False
				list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

	return list_a

print(bubble([4,5,7,1,4,6,8,1,4,5,9,6,8,4,6,3,8,9,4]))