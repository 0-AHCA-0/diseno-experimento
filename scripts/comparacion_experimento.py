import pandas as pd 
import numpy as np 

df = pd.read_csv("/home/acha/EsPRo/lab4/diseno-experimento/plantillas/registro_experimento.csv")

print(df.head())
#Registros por ubicacion
df.groupby("ubicacion")["ventas_producto"].mean()
print("")
#Contar los registros de cada ubicacion
print(df["ubicacion"].value_counts())

#Simulacion de la cantidad de tiendas que vamos a tener asociadas a nuestra franquicia 

tiendas = ["Quito_Norte", "Quito_Sur", "Guayaquil_Centro", "Guayaquil_Norte", "Cuenca_Norte", "Cuenca_Sur", "Ambato_Centro", "Loja", "Machala"]
semanas = [1,2,3,4]

rng = np.random.default_rng(1234597)

primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

filas = []

for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo"
    for s in semanas:
        filas.append({"tienda": tienda, "semana": s, "ubicacion": cond if s%2 == 1 else otra})


