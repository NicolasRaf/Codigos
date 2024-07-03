-- Função para adição
function adicao(a, b)
    return a + b
end

-- Função para subtração
function subtracao(a, b)
    return a - b
end

-- Função para multiplicação
function multiplicacao(a, b)
    return a * b
end

-- Função para divisão
function divisao(a, b)
    if b == 0 then
        return "Erro: Divisao por zero!"
    else
        return a / b
    end
end

-- Função principal para calcular e imprimir o resultado
function calcular(operacao, a, b)
    if operacao == "adicao" then
        return adicao(a, b)
    elseif operacao == "subtracao" then
        return subtracao(a, b)
    elseif operacao == "multiplicacao" then
        return multiplicacao(a, b)
    elseif operacao == "divisao" then
        return divisao(a, b)
    else
        return "Operacao invalida!"
    end
end

-- Solicitar números ao usuário
print("Digite o primeiro numero:")
local num1 = tonumber(io.read())
print("Digite o segundo numero:")
local num2 = tonumber(io.read())

-- Solicitar operação ao usuário
print("\nEscolha a operacao desejada:")
print("1. Adicao")
print("2. Subtracao")
print("3. Multiplicacao")
print("4. Divisao")

-- Ler a escolha do usuário
local escolha = tonumber(io.read())

-- Realizar a operação escolhida
local resultado
if escolha == 1 then
    resultado = calcular("adicao", num1, num2)
elseif escolha == 2 then
    resultado = calcular("subtracao", num1, num2)
elseif escolha == 3 then
    resultado = calcular("multiplicacao", num1, num2)
elseif escolha == 4 then
    resultado = calcular("divisao", num1, num2)
else
    resultado = "Escolha invalida!"
end

-- Exibir o resultado
print("Resultado: ", resultado)
