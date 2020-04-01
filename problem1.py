def sum_of_multiples(n):
	return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

def test():
	assert sum_of_multiples(10) == 23
	
test()
