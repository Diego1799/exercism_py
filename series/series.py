def slices(series, length):
    longitud = len(series)
    if length > longitud or length <= 0:
        raise ValueError('La longitud tiene que ser mayor a cero y menor que {longitud+1} con la serie.')
    return [series[x:x + length] for x in range((longitud - length)+1)]
