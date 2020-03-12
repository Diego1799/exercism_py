def proteins(strand):
    lista = {"AUG": "Methionine", "UUU": "Phenylalanine",
             "UUC": "Phenylalanine",
             "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine",
             "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
             "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine",
             "UGC": "Cysteine", "UGG": "Tryptophan", "UAA": "",
             "UAG": "", "UGA": ""}
    proteinas = []
    for i in range(0, len(strand), 3):
        proteinalista = lista.get(strand[i:i+3])
        if(proteinalista == ""):
            return proteinas
        else:
            proteinas.append(proteinalista)
    return proteinas
