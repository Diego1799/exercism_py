def convert(number):
    sonido = ""
    if number % 3 == 0:
        sonido += "Pling"
    if number % 5 == 0:
        sonido += "Plang"
    if number % 7 == 0:
        sonido += "Plong"

    return sonido if sonido != "" else str(number)
