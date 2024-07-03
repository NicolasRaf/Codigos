
import { escreva,pergunta,get_positive_number } from "./Funções_API/io.js"

function main() {

   //Apresentação 
   let mensagem = `\n[----------Gerador de Senhas----------]
      `
   escreva(mensagem)

   //Entrada
    const num_Digitos = get_positive_number("Informe a quantidade de digitos da senha desejada: ")

   //Saída

    mensagem = `
      =======================================
         A senha escolhida foi: ${fazer_Senha(num_Digitos, 0)}
      =======================================

      `
    escreva(mensagem)
      if(pergunta("Finalizar Programa?(Digite algo) "))
       console.clear()
}

//Processamento

function fazer_Senha (num,num_anterior) {
    let senha = ""
    let num_Atual = 0
    let num_Digitos = 0
    let confi = 0

    while (num_Digitos < num) {
      
        num_anterior = num_Atual
        num_Atual = Math.floor(Math.random() * 10)
        

      if (num_Atual !== 0 && num_Atual !== (num_Atual - 1) && num_Atual !== (num_Atual + 1) && num_Atual !== num_anterior) {
         senha += String(num_Atual)
         num_Digitos++
     }

      if (num_Digitos === num) {
         escreva(`\nA senha Atual é ${senha} `)
         confi = get_positive_number("Deseja outra senha?(1-sim/2-não) ") 
     }

      if (confi === 1) {
         senha = ""
         num_Digitos = 0
         return fazer_Senha(num,num_Atual)
     }

    }

   return senha
}

main()