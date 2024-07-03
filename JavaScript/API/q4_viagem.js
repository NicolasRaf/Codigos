
import { get_positive_number,escreva,pergunta } from "./Funções_API/io.js"

function main() {
    
    //Apresentação
        let mensagem = `\n[-----------Milhas Aéreas-----------]\n`
        escreva(mensagem)

    //Entrada
        const origem = pergunta("Informe o local de origem: ")
        const destino = pergunta("Informe o local de destino: ")
        const preço_Reais = get_positive_number("Digite o preço em Reais do site: ")
        const valor_Milhas = get_positive_number("Digite o valor em Milhas do site: ")

    //Saída
        mensagem = (`
       ==================================================
        --> Preço em Reais: ${preço_Reais.toFixed(2)}
        --> Preço de Milhas Padrão: 
        --> Preço de Milhas Baratas: 

        A melhor opção é
       ==================================================
        `)

        escreva(mensagem)

        if (pergunta(`Finalizar Programa?(Digite Algo): `))
            console.clear()

}

//Processamento


d
main()