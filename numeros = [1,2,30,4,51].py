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
del valores [2]
personas={
    "personas1":{
        "nombre":"juan",
                 "edad": 30,
                 "ciudad":"maadrid"
                 },
                 "persona2": {"nombre":"maria","edad":28,"ciudad":"barcelona"}}

datos=personas^["personas1"]
datos2=personas["personas2"]
print(datos)
print(datos2)
print(datos2["edad"])

#MODIFICAR UN VALOR DENTRO DEL DICCIONARIO 
personas ["personas1"]["edad"]=40
#ACCEDER A UN ELEMENTO 
print(personas["personas1"]["edad"])
#RECORRER UN DIC 
