def roman(number):
    romanos = (
    ( 'M',  1000 ), ( 'CM',  900 ),
    ( 'D',   500 ), ( 'CD',  400 ),
    ( 'C',   100 ), ( 'XC',   90 ),
    ( 'L',    50 ), ( 'XL',   40 ),
    ( 'X',    10 ), ( 'IX',    9 ),
    ( 'V',     5 ), ( 'IV',    4 ),
    ( 'I',     1 ))
    
    numerosr = ""
    for romano, arabico in romanos:
        while number >= arabico:
            numerosr += romano
            number -= arabico
    return numerosr