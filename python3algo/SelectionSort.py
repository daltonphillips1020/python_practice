# trys to find the minimum value in the list
# sets the first value as minimum compares it to every number to the right
# if it finds one that is lower then the initall value set it will assign that value to the new minimum
# once it assigns the new minimum value it moves that value into a new sub list of sorted items
# leaving the items left over as the unsorted items (prevents haveing to sort items that have already been sorted)
# this will continue untill the list is completly sorted

def selection_sort(list_a):
	indexing_length = range(0, len(list_a)-1)

	for i in indexing_length:
		min_value = i

		for j in range(i+1, len(list_a)):
			if list_a[j] < list_a[min_value]:
				min_value = j

		if min_value != i:
			list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

	return list_a

print(selection_sort([2,7,5,4,2,6,8,4,2,6,4,0,1,7,0,6,8,7,6,2,1,1,4,3,]))