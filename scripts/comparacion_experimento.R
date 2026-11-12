# Carga de datos de la simulacion
df <- read.csv('plantillas/resultado_simulacion.csv', stringsAsFactors = FALSE)

# Vista previa y promedio de ventas por ubicacion
print(head(df))
print(aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean))

# Contar los registros de cada ubicacion
print(table(df$ubicacion))

# Efecto de promocion simultanea en Guayaquil_Centro semana 1
df$promocion_simultanea[df$tienda == 'Guayaquil_Centro' & df$semana == 1] <- 'si'
df$ventas_producto[df$promocion_simultanea == 'si'] <- df$ventas_producto[df$promocion_simultanea == 'si'] + 180

# Analisis pareado: promedio por tienda y ubicacion
media_tienda <- tapply(df$ventas_producto, list(df$tienda, df$ubicacion), mean)

# Diferencia entre pasillo principal y ubicacion habitual por tienda
diferencias <- media_tienda[, 'pasillo_principal'] - media_tienda[, 'habitual']

media <- round(mean(diferencias), 2)
dev <- round(sd(diferencias), 2)
print(media)
print(dev)

# Calculo del intervalo de confianza al 95%
n <- length(diferencias)
t_crict <- qt(0.975, df = n - 1)
ic_inf <- media - (t_crict * dev / sqrt(n))
ic_sup <- media + (t_crict * dev / sqrt(n))
cat(sprintf("%f - %f\n", ic_inf, ic_sup))

# Prueba t pareada y p-value
prueba <- t.test(media_tienda[, 'pasillo_principal'], media_tienda[, 'habitual'], paired = TRUE)
print(prueba$conf.int)
cat(sprintf("%.10f\n", prueba$p.value))
