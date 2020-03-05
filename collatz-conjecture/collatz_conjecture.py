def steps(number):
    pasos=0
    if number==1:
        return pasos
    if number>0:
        while number!=1:
            if number % 2 == 0:
                number = number/2
            else:
                number = (3*number)+1
            pasos+=1
        return pasos
    else:
        raise ValueError(ValueError)