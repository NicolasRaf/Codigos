import fs from "fs";
import {ask,getNumberInRange, aksLetter, getNumberPositive} from "./Funções/io.js";

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
    let count = 0;

    for (let letter of word){
        count++;
    }
    return count;
}   

function wordsGreaterThan(lines, size){

    for (let word of lines){
        if (getLength(word) - 1 >= size){
            console.log(`${getLength(word) - 1} - ${word}`);
        }
    }
}

function hasNoLetter(lines, letter){
    let wordsAmount = lines.length - 1;
    let wordsWithoutLetter = 0;

    for (let word of lines){
        let hasLetter = false;
        for (let i of word){
            if (i === letter || i.charCodeAt(0) === letter.charCodeAt(0) + 32){
                hasLetter = true;
                break;
    
            }
        }   
        if (! hasLetter){
            wordsWithoutLetter++ 
            console.log(word);
        }
    }
    let wordsPercent = (wordsWithoutLetter/wordsAmount) * 100;
    console.log(`>>> ${wordsPercent.toFixed(1)}% das palavras não possuem "${letter}" <<<`);

    return wordsWithoutLetter;
}

function avoids(lines){
    let bannedLetters = ask("Digite as letras proibidas juntas: ")

    for (let letter of bannedLetters){
    
    }
}



function showMenu(){
    console.clear();

    console.log(`
    ------------------------- WorldPlay --------------------------   

      [1] Palavras com 20+ Letras    [6]  Palavras com 20+ letras 
      [2] Palavras sem Letra X       [7]  Palavras com 20+ letras 
      [3] Letras Proibidas           [8]  Palavras com 20+ letras 
      [4] Palavras com 20+ letras    [9]  Palavras com 20+ letras 
      [5] Palavras com 20+ letras    [10] Finalizar Execução                                                                               
    `);

    let option = getNumberInRange("Selecione uma opção: ",1,10,"\nSelecione uma opção valida!!\n");
    console.clear();
    
    return option;
}

function main(){
    let option = showMenu();

    const data = fs.readFileSync('words.txt', 'utf-8');
    const lines = data.split("\n");

    while (option !== 10){
        let size = 0
        let letterToHide = ""

        if (option === 1){
            wordsGreaterThan(lines,20);
        } else if (option === 2){
            letterToHide = (letterToHide === "") ? aksLetter("Digite uma letra: ") : letterToHide
            hasNoLetter(lines,letterToHide);
         }else if (option === 3){
            avoids(lines)
         }

        ask(`\nContinuar(Press Enter)`);
        option = showMenu();

        
    }
}

main();