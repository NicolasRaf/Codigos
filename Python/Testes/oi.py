from PIL import Image, ImageDraw, ImageFont

# Criando a imagem e o contexto de desenho
img = Image.new("RGB", (1000, 600), "white")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

# Função para desenhar as entidades (esta função precisa estar definida)
def draw_entity(x, y, width, height, name, attributes):
    draw.rectangle([x, y, x + width, y + height], outline="black", width=2)
    draw.text((x + 5, y + 5), name, fill="black", font=font)
    for i, attr in enumerate(attributes):
        draw.text((x + 5, y + 25 + i*15), attr, fill="black", font=font)

# Função para desenhar os relacionamentos
def draw_relationship(x, y, width, height, name, from_pos, to_pos):
    # Desenha o losango
    draw.polygon([x, y - height, x - width, y, x, y + height, x + width, y], outline="black", width=2)
    # Adiciona o nome do relacionamento
    draw.text((x - 30, y - 10), name, fill="black", font=font)
    # Desenha as linhas para conectar as entidades
    draw.line([from_pos, (x, y)], fill="black", width=2)
    draw.line([to_pos, (x, y)], fill="black", width=2)

# Desenhando as entidades
draw_entity(200, 50, 200, 100, "Cidade", ["sigla (PK)", "nome_cidade", "estado", "numero_habitantes"])
draw_entity(700, 50, 200, 100, "Ônibus", ["num_sequencial (PK)", "chassi", "placa", "ano_fabricacao", "quilometragem"])
draw_entity(200, 400, 200, 100, "Empresa de Turismo", ["codigo_empresa (PK)", "nome", "razao_social", "telefone"])
draw_entity(700, 400, 200, 140, "Aluguel", ["codigo_aluguel (PK)", "data_saida", "valor", "num_sequencial (FK)", "codigo_empresa (FK)", "cidade_origem (FK)", "cidade_destino (FK)"])

# Desenhando os relacionamentos
draw_relationship(450, 150, 50, 30, "Origem", (400, 100), (700, 100))
draw_relationship(450, 200, 50, 30, "Destino", (400, 100), (700, 200))
draw_relationship(450, 500, 50, 30, "Aluga", (400, 450), (700, 450))

# Salvando a imagem final
image_path = "/mnt/data/diagrama_er_onibus_formatos_corretos.png"
img.save(image_path)

image_path
