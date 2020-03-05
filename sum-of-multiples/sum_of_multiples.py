def sum_of_multiples(limit, multiples):
    numero = 0
    for i in range(limit):
        for multiplo in multiples:
          if multiplo == 0:
            break
          if i % multiplo == 0:
            numero += i
            break
    return numero