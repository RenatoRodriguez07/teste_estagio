string = input("Digite uma string: ")

quantidade_a = string.count('a') + string.count('A')

if quantidade_a > 0:
  print(f" A letra 'a' aparece {quantidade_a} vezes na string.")
else:
  print("A letra 'a' não foi encontrada na string.")