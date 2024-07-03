import matplotlib.pyplot as plt
import numpy as np

# Dados para A e B
dados = np.array([[500, 1000, 2000, 3500],  # Dados para A
                  [500, 1000, 2000, 3500]])  # Dados para B

# Ajustando o terceiro quartil para 2000
dados[:, 2] = 2000

# Criar o boxplot
plt.boxplot(dados.T, patch_artist=True)

# Adicionar rótulos aos eixos
plt.xticks([1, 2], ['A', 'B'])
plt.ylabel('Valor')
plt.title('Boxplot')

# Exibir o gráfico
plt.show()

print(dir(np))

