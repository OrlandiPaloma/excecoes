a=2
b=0
#como não existe divisão por zero, o programa vai dar erro, por isso aplicamos a exceção.

try:
  print(a/b)
except:
  print("Não é permitida divisão por zero")


#Note que se tiver algo após, o programa vai continuar a rodar normalmente.
print(a/a)
