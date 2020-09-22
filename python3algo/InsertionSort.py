# takes unsorted sequence and sorts them in to two sub lists
# one list is for sorted values
# the other will be for un-sorted values
# all values will origonate in the un_sorted sub list except for the first value
# from left to right each value will get added to the sorted sublistand compared to the value to the left of it
# if the value of the item to the left is higher then the item added then it will swap postions 
# the item will keep getting moved to the left in the sorted sublist untill it finds a value that it is lower then
# this will let the algo, know that the value is in the correct place

def insertion_sort(list_a):
	indexing_length = range(1, len(list_a))
	for i in indexing_length:
		value_to_sort = list_a[i]

		while list_a[i-1] > value_to_sort and i>0:
			list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
			i =  i-1


	return list_a


print(insertion_sort([2,3,5,6,3,2,5,3,9,7,5,3,7,1,9,5,8,6,]))