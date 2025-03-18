numeros = [1,2,30,4,51]
for numero in numeros: 
    cuadrado=numero**2
    print(f"el cuadrado de {cuadrado}es {cuadrado}")

print(numeros[4])
#TRATAMIENTO DE CADENAS 

apellido="MENDOZA"
frace="hola esta es una frace"
longitud=len(frace)
print(longitud)
print(apellido[5])
palabras=frace.split()
print(palabras)
 
print(palabras[0])
palabras[1]="chau"
print(palabras)
mayuscula=frace.upper
print (mayuscula)
minusculas=frace.lower
print (minusculas)

valores=[2, 4,50,36]
valores.append(8)
print(valores)