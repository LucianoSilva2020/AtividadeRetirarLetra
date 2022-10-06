import os 
os.system('cls')
from re import A
from unittest import result


def stringSemLetra(letra, palavra):
    resultado = ''
    for percorrer in palavra:
        if(percorrer != letra):
            resultado = resultado + percorrer
    return resultado

letraDigitada = input('Digite uma letra:')
palavraDigitada = input('Digite uma palavra:')
result = stringSemLetra(letraDigitada.lower(), palavraDigitada.lower())
print(f'O resultado é {result}')
