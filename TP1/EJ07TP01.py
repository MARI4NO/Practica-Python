'''
Solicite el valor de un ángulo en Radianes 
conviértalo a grados Sexagesimales y luego 
a Centesimales. Muestre los resultados en 
pantalla. Fórmula de conversiones: 
sexadecimal = valorEnRadian * 180 / Pi, 
centesimal = valorEnRadian * 200 / Pi
'''
PI=3.14
angulo=float(input('Ingrese el angulo en radianes: '))
sexadecimal= angulo *180 /PI
centesimal = angulo * 200 / PI
print('Valor en Sexadecimal: ',sexadecimal ,'Valor en centesimal', centesimal)