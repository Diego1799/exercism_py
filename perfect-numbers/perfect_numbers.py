def classify(number):
    if number <= 0:
        raise ValueError("No 0 or negative numbers allowed")

    divisors = [x for x in range(1, number) if number % x == 0]
    aliqout_sum = sum(divisors)

    if aliqout_sum == number:
        return 'perfect'
    elif aliqout_sum >= number:
        return 'abundant'
    else:
        return 'deficient'
