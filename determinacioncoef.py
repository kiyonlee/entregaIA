import numpy as np
#insertar caracteristicas y etiquetas del ejemplo resistencia
caracteristicas = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
etiquetas = np.array([0.169610271922408, 0.283395812542308, 0.386358737510785, 0.470227872390909, 0.433281293764675, 0.600267648212653, 0.738338980436742, 0.790315020494445, 0.877464268422459, 0.84356446225183, 0.96443891694455])
etiq_media=etiquetas.mean() #Media de los valores de las etiquetas
var=np.zeros(12)
err=np.zeros(12)
Th0=0.0399999999999352 #theta0
Th1=0.15999999999993264 #theta1
mod_x = Th0 + Th1*caracteristicas #Modelo lineal con theta1 y theta0 calculados en clase
for a in range(len(etiquetas)):
err[a] = pow(etiquetas[a]-mod_x[a],2) #calculo coeficiente de error para cada etiqueta
var[a] = pow(etiquetas[a]-etiq_media,2) #calculo variacion de cada etiqueta
Coeficiente_de_determinacion=1-(err.sum()/var.sum()) #calculo del coeficiente de determinacion con la relacion entre el coeficiente de error y la varianza
print(Coeficiente_de_determinacion) #imprimir el valor calculado
