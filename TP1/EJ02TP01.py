#Resolver expresiones algebraicas
PI =3.14 
x= float(input('Ingrese el valor de x:  '))
y= float(input('Ingrese el valor de y:  '))
z= float(input('Ingrese el valor de z:  '))

opcion=int (input('seleccione expresion algebraica 1 / 2 '))
if opcion == 1:
    print(3*(x/y) + (-y/z)*5)
else :
    if(y==z):
        print('No se puede realizar division por cero, selecciones valores distintos para Y & Z')
    else:
        print(PI*(x*x)-(1/2)*((x/(y-z)) ** (1/3)))
