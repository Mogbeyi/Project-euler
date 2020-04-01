def sum_even_fib():
	max_value = 4000000
	prev = 0
	curr = 1
	even_total = 0

	while (prev < max_value):
		prev, curr = curr, prev + curr
		if is_even(curr):
			even_total += curr

	return even_total

def is_even(n):
	return n % 2 == 0

def test():
	assert sum_even_fib() == 4613732

test()

