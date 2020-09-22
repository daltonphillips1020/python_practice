# looks through a already sorted sequence and determines if a item youre looking for is in that sequence or not
# selects mid point of sequence
# if the value is higher then the mid point in the sequence then it will serch through the items on the right of the mid point
# this will continue to happen through the lists untill the value you are looking for is found 
# or untill there are no more items in the sequence to look through 
# if the value is found before the algo. is through the sequence then the algo. will hault and return the postion of the value

def binary_search(sequence, item):
	begin_index = 0
	end_index = len(sequence) - 1

	while begin_index <= end_index:
		midpoint = begin_index + (end_index - begin_index) // 2
		midpoint_value = sequence[midpoint]
		if midpoint_value == item:
			return midpoint

		elif item < midpoint_value:
			end_index = midpoint_value - 1

		else:
			begin_index = midpoint_value + 1

	return None

sequence_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
item_a = 17

print(binary_search(sequence_a, item_a))