import { question } from "readline-sync";

const pontos = question("Digite 3 numeros: ").split(" ").map(Number)
const ponto1 = pontos[0]
console.log(`O primeiro numero da lista é ${pontos}`)