#determinante de uma matriz 2x2 nivel medio exercicio 2
# calculando o determinante 
def determ(matriz):
    a, b, c, d = matriz[0][0], matriz[0][1], matriz[1][0], matriz[1][1]
    return a * d - b * c
 # preenchimento de matriz 
mat= [[0, 0], [0, 0]]
for i in range(2):
	for j in range(2):
		mat[i][j]=int(input('digute o numero '))
	print()
  # exibindo o determinante 
resultado = determ(mat)
print(f"O determinante da matriz é: {resultado}")'''
