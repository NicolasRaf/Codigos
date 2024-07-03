import numpy as np

# Valores fornecidos
valores = [2, 3, 6, 4, 3, 6, 2, 4, 5, 3, 5, 7, 5, 2, 2, 5]

# Calculando a média
media = np.mean(valores)

# Calculando a variância
variancia = np.var(valores)

# Calculando o desvio padrão
desvio_padrao = np.std(valores)

# Calculando a diferença entre a média e cada valor em módulo
diferenca_media = [(media - x) for x in valores]

# Calculando o quadrado de cada valor
quadrado_valores = [x ** 2 for x in valores]

# Calculando a soma dos quadrados dos valores
soma_quadrados = sum(quadrado_valores)

# Exibindo os resultados
print("Média:", media)
print("Variância:", variancia)
print("Desvio Padrão:", desvio_padrao)
print("Diferença entre a média e cada valor em módulo:", diferenca_media)
print("Quadrado de cada valor:", quadrado_valores)
print("Soma dos quadrados dos valores:", soma_quadrados)
