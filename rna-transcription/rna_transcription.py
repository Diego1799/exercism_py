def to_rna(dna_strand):
     cambio= ""
     for i  in dna_strand:
      if i == "C":
       cambio += "G"
      if i == "G":
       cambio+= "C"
      if i == "T":
       cambio+= "A"
      if i == "A":
       cambio+= "U"
     return cambio