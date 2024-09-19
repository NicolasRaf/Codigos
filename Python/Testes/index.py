## Coluna na Matriz ##

import os
import random

def doReduce(vector, work, initialValue: int = 0):
    accumulated = initialValue

    for i in vector:
        accumulated = work(accumulated, i)

    return accumulated


def main():

    matrix = []
    vector = []

    for i in range(16):
        vector.append(random.randint(0, 25))

        if (i + 1) % 4 == 0:
            matrix.append(vector)
            vector = []

    currentline = 0
    currentColum = 0

    for lines in matrix:
        for number in lines:
            os.system("cls")
            matrix[currentline][currentColum] = int(input(f"Posição [{currentline}]:[{currentColum}] -> "))

            currentColum += 1
        
        currentColum = 0
        currentline += 1

    print("-" * 20)

    for line in matrix:
      print(" ".join(f"{num:3}" for num in line))

    print("-" * 20)
    
main()