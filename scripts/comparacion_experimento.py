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

#sorteo de la condicion inicial
rng = np.random.default_rng(1234597)
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))
print(primera)
filas = []

for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo"
    for s in semanas:
        filas.append({"tienda": tienda, "semana": s, "ubicacion": cond if s%2 == 1 else otra})

diseno = pd.DataFrame(filas)
#print(filas)

#simulacion ejecucion 
rng = np.random.default_rng(1234598)
efecto_tienda = dict(zip(tiendas, rng.normal(1100,120,len(tiendas))))
efecto_semana = {1: 0, 2: 30, 3: 60, 4: 90 }
#print(efecto_tienda)
diseno['ventas_producto'] = (diseno['tienda'].map(efecto_tienda) + diseno['semana'].map(efecto_semana) 
                              + (diseno['ubicacion'] == "pasillo_principal") * 220
                              + rng.normal(0,90, len(diseno))
                              ).round(0).astype(int)

#print(diseno) 

diseno['promocion_simultanea'] = 'no'

#El loc lo que hace es que se cumpla una cierta condicion, despues de la coma es la columna en la que se va a poner 
diseno.loc[(diseno['tienda'] == 'Guayaquil Centro') & (diseno['semana'] == 1), 'promocion_simultanea'] = 'si'
diseno.loc[diseno['promocion_simultanea'] == 'si', 'ventas_producto'] += 180

#print(diseno)

#Analisis pareado: una fila por tienda con sus condiciones
piv = diseno.groupby(['tienda','ubicacion'])['ventas_producto'].mean().unstack()
piv['diferencia'] = piv['pasillo_principal'] - piv['habitual']

media = round(piv['diferencia'].mean(), 2)
dev = round(piv['diferencia'].std(ddof=1), 2)
print(media)
print(dev)
#print(piv)


