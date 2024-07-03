# Dados fornecidos: valores de X e Y
valores_X = [78, 17, 42, 67, 45, 76, 54, 63, 80, 38, 25, 68, 55, 96, 75, 8]
valores_Y = [83, 8, 38, 69, 52, 77, 55, 65, 81, 40, 23, 64, 54, 98, 83, 3]

# Calcular o quadrado de X
quadrados_X = [x ** 2 for x in valores_X]

# Calcular o quadrado de Y
quadrados_Y = [y ** 2 for y in valores_Y]

# Calcular o produto de X e Y
produtos_XY = [x * y for x, y in zip(valores_X, valores_Y)]

# Calcular o somatório de X
soma_X = sum(valores_X)

# Calcular o somatório de X ao quadrado
soma_X_quadrado = sum(x ** 2 for x in valores_X)

# Calcular o somatório de Y
soma_Y = sum(valores_Y)

# Calcular o somatório de Y ao quadrado
soma_Y_quadrado = sum(y ** 2 for y in valores_Y)

# Calcular o somatório dos produtos entre X e Y
soma_produtos_XY = sum(x * y for x, y in zip(valores_X, valores_Y))

# Exibir os resultados
print("Quadrado de X:", quadrados_X)
print("Quadrado de Y:", quadrados_Y)
print("Produto de X e Y:", produtos_XY)
print("Somatório de X:", soma_X)
print("Somatório de X ao quadrado:", soma_X_quadrado)
print("Somatório de Y:", soma_Y)
print("Somatório de Y ao quadrado:", soma_Y_quadrado)
print("Somatório dos produtos (X * Y):", soma_produtos_XY)


import numpy as np

# Dados fornecidos: valores de X e Y
valores_X = [78, 17, 42, 67, 45, 76, 54, 63, 80, 38, 25, 68, 55, 96, 75, 8]
valores_Y = [83, 8, 38, 69, 52, 77, 55, 65, 81, 40, 23, 64, 54, 98, 83, 3]

# Calcular a correlação linear de Pearson
correlacao_pearson = np.corrcoef(valores_X, valores_Y)[0, 1]

# Exibir a correlação
print("Correlação linear de Pearson:", correlacao_pearson)