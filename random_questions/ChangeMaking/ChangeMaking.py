# Determine the most efficent way to calculate how many coins you will get when getting back change
# EX. if you get back 75cents then the best out come is 3 (quarters)
# EX. if you get back 32cents then the best out come is 5 (3 dimes, 2 pennies)

def num_coins(cents):
	coins = [25, 10, 5, 1]
	count = 0
	for coin in coins:
		while cents >= coin:
			cents = cents - coin
			count = count + 1

	return count

print(num_coins(57))