'''Solicite el ingreso de una
 cantidad de pesos Argentinos,
  dar su equivalente en dólares
   y en euros. Se sabe que 1 dólar = 
   202,30 pesos y 1 euro = 214,30 pesos (
    formatee 
los resultados a 3 decimales).

'''
plata=float(input('Ingrese el monto'))
print('Valor en Dolares: ' , round(plata / 202.30 , 2))
print('Valor en Euros: ', round(plata / 214.30, 2))
