"""numeros=(1,2,3,4,5,6)
for numero in numeros:
    print (numero)"""
#break para romper continue para hacer lo siguiente de la condicion
print ("introduce un numero para hacer la tabla de multiplicar")
x=int(input())
y=range(0,11)
for numero in y :
    z=int(x*numero)
    print (f"la multiplicacion de {x} por {numero} da como resultado {z} " )

"""#while
print ("introduce un numero para hacer la tabla de multiplicar")
x=int(input())
y=1
while int(y)<=10 :
    z=int(x*y)
    print (f"la multiplicacion de {x} por {y} da como resultado{z} " )
    y=y+1
     """