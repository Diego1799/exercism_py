def is_valid(isbn):
    isbn = list(isbn.replace("-", "").upper())
    if len(isbn) != 10:
        return False
    if isbn[-1] == "X":
        isbn[-1] = "10"
    resultado = 0
    for i in range(10):
        try:
            resultado += int(isbn[i]) * (10-i)
        except ValueError:
            return False
    return resultado % 11 == 0
