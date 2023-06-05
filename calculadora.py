import sys
import argparse
import pandas as pd
import re

#n1 = int(sys.argv[1])
#n2 = int(sys.argv[2])
#operador = sys.argv[3]

parser = argparse.ArgumentParser()
parser.add_argument('operaciones')
parser.add_argument('resultados')

# Obtener los argumentos de los archivos
args = parser.parse_args()
operaciones = args.operaciones
resultados = args.resultados


def calculadora(n1, n2, operador):
    if operador == '+':
        resultado = n1 + n2
    elif operador == '-':
        resultado = int(n1) - int(n2)
    elif operador == '*':
        resultado = int(n1) * int(n2)
    elif operador == '/':
        if n2 != 0:
            resultado = int(n1) / int(n2)
        else:
            return "Error: División por cero no permitida."
    else:
        return "Error: Operador no válido."
    
    
    return resultado

def proc_archivos(operaciones, resultados):
     # Aquí puedes realizar las operaciones que desees con los archivos
    

    df = pd.read_csv(operaciones)
    resultado = "Resultados: \n"

    for i in range(len(df)):
        df[['n1', 'operador', 'n2']] = df['Operacion'].str.split('(\+|-|\*|/)', expand=True, n=2)
        try:
           n1 = int(df['n1'].iloc[i])
           n2 = int(df['n2'].iloc[i])
        except ValueError:
           print("Error: alguno de los valores no es un número o no se utiliza el operador correcto. Repasa el archivo entrada.txt")
           break
        operador = df['operador'].iloc[i]
        resultado += f"{df.at[i, 'Operacion']} = {calculadora(n1,n2,operador)}\n" 
        
        

    with open(resultados, 'w') as archivo:
        archivo.write(resultado)

proc_archivos(operaciones, resultados)
