def is_pangram(sentence):
   oracion = sentence.lower()
   abecedario = 'abcdefghijklmnopqrstuvwxyz'
   for i in abecedario:
       if i not in oracion:
           return False
   return True
