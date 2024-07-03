# Dados fornecidos
n = 16
sum_x1 = 178.6
sum_x2 = 1005.6
sum_x1_squared = 2159.8
sum_x2_squared = 74175.9
sum_x1_x2 = 10018.9

# Cálculo da média
mean_x1 = sum_x1 / n
mean_x2 = sum_x2 / n

# Cálculo da variância
var_x1 = (sum_x1_squared / n) - (mean_x1 ** 2)
var_x2 = (sum_x2_squared / n) - (mean_x2 ** 2)

# Cálculo da correlação
cov_x1_x2 = (sum_x1_x2 / n) - (mean_x1 * mean_x2)
correlation = cov_x1_x2 / ((var_x1 ** 0.5) * (var_x2 ** 0.5))

print(f"Média da Penetração de água: {mean_x1}")
print(f"Variância da Penetração de água: {var_x1}")
print(f"Média da Proporção de poros pequenos: {mean_x2}")
print(f"Variância da Proporção de poros pequenos: {var_x2}")
print(f"Correlação entre Penetração de água e Proporção de poros pequenos: {correlation}")
