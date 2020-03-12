def factors(value):
    factores = [] 
    n = 2
    while value > 1:
        while (value % n) == 0:
            factores.append(n)
            value /= n
        n += 1
    return factores
