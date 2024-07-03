#O desafio é escrever duas funções da forma mais simples possível:
#- A primeira deve converter um horário militar para AM/PM
# A segunda deve converter um horário AM/PM para militar 

def main():
    #Apresentação
    print("\n[---------------Conversor Horário AM/PM e Militar---------------]")
    print("Obs: Em caso de conversão AM/PM para militar escreva junto o período(\"AM\" ou \"PM\")\n")

    #Entrada32
    op = input("Digite o horário (hh:mm:ss): ")

  
    #Saída
    if validação(op):
        print("\n======================================================")
        if "AM" in op or "PM" in op or "am" in op or "pm" in op:
            turno = op[9:11]
            onlyHour = op[0:9]
            horario = list(map(int, (onlyHour).split(":")))
            print(ampm_to_militar(horario[0],horario[1],horario[2],turno))
        else:
            onlyHour = op[0:9]
            horario = list(map(int, (onlyHour).split(":")))
            print(militar_to_ampm(horario[0],horario[1],horario[2]))
        print("========================================================")

#Processamento
def militar_to_ampm(hr,min,seg):
    turno = ""

    if hr >= 12:
        turno = "PM"
    else:
        turno = "AM"

    if hr == 0:
        hr = 12
    elif hr > 12:
        hr -= 12
    
    return (f"O horário em formato AM/PM é {hr}:{min:02d}:{seg} {turno}")

def ampm_to_militar(hr,min,seg,turno):

    if turno == 'AM' or turno == 'am':
        if hr == 12:
            hr = 0
    elif turno == 'PM' or turno == 'pm':
        if hr != 12:
            hr += 12

    return (f"O horário em formato militar é {hr}:{min:02d}:{seg}")

def validação(op):
    entrada = str(op)
    if len(entrada) < 8:
        print("Horário Invalido")
        return False
    
    onlyHour = entrada[0:9]
    
    try:
        horario = list(map(int, (onlyHour).split(":")))
        return True
    except:
        print("Horário Invalido")
        return False

main()  