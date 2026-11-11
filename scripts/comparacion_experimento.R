library(readr)
df <- read.csv('plantillas/resultado_simulacion.csv', stringsAsFactors = FALSE)
print(aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean))
#print(df)

#print(df[, c("tienda", "semana", "ubicacion", "ventas_producto", "promocion_simultanea")])

media_tienda <- tapply(df$ventas_producto, list(df$tienda, df$ubicacion), mean)

diferencias <- media_tienda[, 'pasillo_principal'] - media_tienda[, 'habitual']
print(mean(diferencias))

prueba <- t.test(media_tienda[,'pasillo_principal'], media_tienda[, 'habitual'], pained = TRUE)

print(prueba$conf.int)
print(prueba$p.value)