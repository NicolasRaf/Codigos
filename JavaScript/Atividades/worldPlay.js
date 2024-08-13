import fs from "fs";
import {ask, getNumberInRange} from "./Funções/io.js";

function getSlice(text, remove){
    let wordSliced = "";

    for (let letra of text){
        if (letra !== remove){
            wordSliced += letra;
        }
    }

    return wordSliced;
}

function getLength(word){
    let count = 0

    for (let letter of word){
        count++
    }
    return count
}   

function wordsGreaterThan(word, size){
    if (getLength(word) - 1 > size){
        console.log(`${getLength(word) - 1} - ${word}`);
    }

}

function hasNoE(word, letter){
    let haveLetter = false

    for (let i of word){
        if (i === letter){
            haveLetter = true   
        }
    }

    if (!haveLetter){
        console.log(word);

    return
    }
}

function showMenu(){
    console.clear();

    console.log(`
    ------------------------- WorldPlay --------------------------   

      [1] Palavras com 20+ letras    [6]  Palavras com 20+ letras 
      [2] Palavras sem letra "e"     [7]  Palavras com 20+ letras 
      [3] Palavras com 20+ letras    [8]  Palavras com 20+ letras 
      [4] Palavras com 20+ letras    [9]  Palavras com 20+ letras 
      [5] Palavras com 20+ letras    [10] Sair                                                                               
    `);

    let option = getNumberInRange("Selecione uma opção: ",1,10,"Selecione uma opção valida!!");
    console.clear();
    
    return option;
}

function main(){


    let option = showMenu();

    const data = fs.readFileSync('words.txt', 'utf-8');
    const lines = data.split("\n");

    while (option !== 10){

        for (let word of lines){

            if (option === 1){
                wordsGreaterThan(word,20);
            } else if (option === 2){
                hasNoE(word,"e");
            }

        }
        ask(`\nContinuar(Press Enter)`);
        option = showMenu();

        
    }
}

main();