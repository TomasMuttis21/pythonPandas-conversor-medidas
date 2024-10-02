import pandas as pd

#Dataframe es la info basica con el nombre de las piezas y centrimetos

data ={
    "Piezas:" : ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros": [40,120,60,30,180]
}

df = pd.DataFrame(data)

##Guardar el Dataframe en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)
