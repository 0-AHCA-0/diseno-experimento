# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** ___ · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

*Hipótesis que el experimento pueda confirmar o refutar (formúlela como una comparación medible entre los grupos).*

## 2. Unidad experimental
semana-tienda (**# de tienda x # de semanas**)
*¿Qué recibe el tratamiento? ¿Cuántas unidades se incluyen?*
semana-tienda (# tienedas x numero de semanas)

- Unidad:
- Número de unidades y justificación:

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): ubicacion del producto 
- **Niveles** (valores del factor): pasillo y habitacion 
- **Tratamiento** (combinación asignada): pasillo durante 1 seman y ubicacion habitual durante otra (grupo de control)

## 4. Grupo de control
El grupo de control en este caso es la tienda pero con el producto dispuesto en la ubicacion actual 

## 5. Aleatorización
sorteo de 20 tinedas a cada grupo (todos en paralelo)
## 6. Respuesta y medición
- Variable respuesta: las ventas semanales en dolares
- Período de medición: 4 semanas 
- Quién registra y cómo (¿ciego?): Mediante el punto de venta, ciego (vendedor no sabria si el producto esta en principal o en habitual)

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | Clima|
| 2. | Evento local|
| 3. | surtido / stock|
| 4. | Cambios en el personal|

## 8. Limitaciones del diseño

- perdida de potencia por promosiones de la competencia 
- canibalizacion de la tienda 
## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?

El pasillo muestra 1335 USD en venta frente a 1040 USD en habitual
- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
No se puede concluir nada en este experimento, ya que se cuenta con muy pocas muestras. En una asignacion real existirian diversos factores que alterarian este y no se han controlado en este experimento de muestra.
- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
