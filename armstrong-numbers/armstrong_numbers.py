def is_armstrong_number(number):
    potencia = len(str(number))
    return sum(int(i)**potencia for i in str(number)) == number 
