# takes a unsorted sequence and sorts it out in ether assending or desending order (asending in this example)
# takes one item in the sequence and making that the pivot point ( the last item in the unsorted sequence )
# then going through the list from left to right the values will get moved into two lists.
# if the value is lower than it will go to the list that is for less than than the pivot point
# if it is higher then it will go to a seperate list that is for more than the pivot point
# after the two lists are sorted then you will know that your pivot point is correctly sorted
# both of the new lists will have to pick a new pivot point and go through the sequence agian with there own sub lists

def quick_sort(sequence):
	length = len(sequence)
	if length <= 1:
		return sequence
	else:
		pivot = sequence.pop()

	items_greater =[]
	items_lower =[]

	for item in sequence:
		if item > pivot:
			items_greater.append(item)

		else:
			items_lower.append(item)

	return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([1,8,5,7,4,2,7,2,5,4,7,2,8,9,5,2,6,8,4,2,1,6,9,0]))