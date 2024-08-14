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

function hasLetter(lines, letter){

    for (let word of lines){
        let hasLetter = false;
        for (let i of word){
            if (i === letter || i.charCodeAt(0) === letter.charCodeAt(0) + 32){
                hasLetter = true;
                continue;
            }
        }
    }
}

function hasNoLetter(lines, letter,show){
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
            let print = show ? console.log(word) : wordsAmount
        }
    }
    let wordsPercent = (wordsWithoutLetter/wordsAmount) * 100;
    console.log(`\n>>> ${wordsWithoutLetter} | ${wordsPercent.toFixed(1)}% das palavras não possuem "${letter}" <<<`)

    return wordsWithoutLetter;
}

function avoids(lines){
    let bannedLetters = ask("Digite as letras proibidas juntas: ")
    let newBanned = ""
    let total = 0

    for (let letter of bannedLetters){
        for (let count = 0; count <= getLength(bannedLetters); count++){
                if (letter === bannedLetters[count] && ! inNewBanned(newBanned,letter)){
                    newBanned += letter
            }
        }
    }

    for (let letter of newBanned){
        total += hasNoLetter(lines, letter,false)
    }   
    console.log(`\n>>>>>> O total de palavas sem as letras são: ${total}`)
}

function inNewBanned(newBan, letter){
     
    for (let i of newBan){
        if (letter === i || letter === " "){
            return true
        }
    }
    return false
}

function usesOnly(){
    let lettersOnly = ask("Digite as letras permitidas juntas: ")
    let newAllow = ""
    
    for (let letter of lettersOnly){
        for (let count = 0; count <= getLength(lettersOnly); count++){
                if (letter === lettersOnly[count] && ! inNewBanned(newAllow, letter)){
                    newAllow += letter
            }
        }
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
            hasNoLetter(lines,letterToHide,true);
         }else if (option === 3){
            avoids(lines)
         }else if (option === 4){
            usesOnly()
         }

        ask(`\nContinuar(Press Enter)`);
        option = showMenu();

        
    }
}

main();