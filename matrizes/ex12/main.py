
#exercicio 5  nivel basico
#funcaobsomar linha e coluna
def somar(matriz):
  #somando cada elemento da linha
  # sum para somar os elementos da linha 
  # zip(*matriz) para transpor a matriz permitindo somar elementos da coluna
    soma_l= [sum(l) for l in matriz]
    
    soma_c = [sum(c) for c in zip(*matriz)]
    
    return soma_l, soma_c
    
mat = [ [0,0,0],[0,0,0],[0,0,0]]
# preenchendo a matriz 
for l in range(3):
	for c in range(3):
		mat=int(input('insira os numeros '))
	print()
soma = somar(mat)
# exibindo a soma das linhas e colunas 
print(f"Soma de cada linha: {soma}")
print(f"Soma de cada coluna: {soma}")
                  
