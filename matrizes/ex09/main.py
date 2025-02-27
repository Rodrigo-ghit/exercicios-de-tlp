#exercio 3 nivel basico                                             
#funcao para somar os elementos 
def soma_mat(matriz):
    soma = 0
    for l in matriz:
        for c in l:
            soma += c
    return soma
#inicializando a matriz 
matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
#preenchendo a matriz 
for i in range(3):
	for j in range(3):
		matriz[i][j]=int(input(f'digite o numero pra [{i+1},{j}] '))
	print()
#verificar a matriz preenchida
print(matriz)
#imprimindo a soma dos elementos 
result= soma_mat(matriz)
print(f"A soma de todos os elementos da matriz é: {result}")'''
