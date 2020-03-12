def prime(positive_number):
	if positive_number < 1:
		raise ValueError("Value Error")
	prime_list = [2]
	num = 3
	while len(prime_list) < positive_number:
		for p in prime_list:
			if num % p == 0:
				break
		else:
			prime_list.append(num)
		num += 2
	return prime_list[-1]
