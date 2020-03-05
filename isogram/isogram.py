def is_isogram(string):   
    exepcion = " ,_-"
    conteo = [i.lower() for i in string if i not in exepcion]
    for i in conteo:
     if conteo.count(i)>1:
      return False
      break 
    else:
         return True
     
        
        def is_pangram(sentence):
   oracion = sentence.lower()
   abecedario = "abcdefghijklmnopqrstuvwxyz"
   for char in abecedario:
       if char not in oracion:
           return False
       return True
