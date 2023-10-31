import pandas as pd

def desanidar(ruta, diccionario):
    df = []
    with open(ruta, encoding='utf-8-sig') as file:
        for linea in file:
            df.append(eval(linea))
    for i in df:
        for clase, valor in i.items():
            diccionario[clase].append(valor)
    diccionario = pd.DataFrame(diccionario)
    return diccionario