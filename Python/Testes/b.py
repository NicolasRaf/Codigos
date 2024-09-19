from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Título do Documento', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)


# Add answers to the PDF
answers = """
1. Total de IDs distintos (1 byte = 8 bits):
O total de IDs possíveis é 2^8 = 256.

2. Total de IDs com exatamente 3 valores “1”:
Isso é uma combinação de 8 bits, escolhendo 3 posições para “1”: C(8,3) = 56.

3. Probabilidade do evento A e B:
- A: A probabilidade de a etiqueta 1 escolher o slot 1 é 1/10 = 0.1.
- B: A probabilidade de a etiqueta 1 não escolher o slot 1 é 1 - 0.1 = 0.9.
Esses eventos são complementares e seguem a distribuição de Bernoulli.

4.1. Valores possíveis para X:
X = 0, 1, 2, 3, 4, 5 (número de etiquetas que podem escolher o slot 1).

4.2. Probabilidade de uma etiqueta escolher o slot 1:
A probabilidade é binomial:
P(X = 1) = C(5,1) * (0.1)^1 * (0.9)^4 = 0.328

4.3. Distribuição de probabilidade de X:
- P(X = 0) = (0.9)^5 = 0.59049
- P(X = 1) = 0.32805
- P(X >= 2) = 1 - (P(X = 0) + P(X = 1)) = 0.08146

4.4. Número máximo de slots para probabilidade de slot vazio ser inferior a 50%:
Utilizando a distribuição binomial, P(X = 0) < 0.5, encontramos o número máximo de slots.

4.5. Número mínimo de slots para probabilidade de colisão ser inferior a 2%:
A probabilidade de colisão é P(X >= 2). Calculamos o número mínimo de slots para que P(X >= 2) < 0.02.

4.6. Escolha da configuração (4.4 ou 4.5):
A escolha depende da análise de custo, onde o sucesso gera R$ 10, o slot vazio custa R$ 0.10 e a colisão R$ 2. 
O cálculo do valor esperado determinará a configuração ideal.
"""

# Adicione o texto ao PDF
pdf.multi_cell(0, 10, answers)

output_path = 'c:/Users/nicol/Documents/Codigos/Python/Testes/output.pdf'
pdf.output(output_path)



