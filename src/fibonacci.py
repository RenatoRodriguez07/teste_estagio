def fibonacci(limit):
  fib_sequence = [0, 1]
  while fib_sequence[-1] < limit:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
  return fib_sequence

def is_in_fibonacci(num):
  fib_sequence = fibonacci(num)
  if num in fib_sequence:
    return f"O número {num} pertence à sequência de Fibonacci."
  else:
    return f"O número {num} NÃo pertence à sequência de Fibonacci."
  
numero = int(input("Informe um número: "))

resultado = is_in_fibonacci(numero)
print(resultado)