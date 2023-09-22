#PROBLEMA 1:
print("\t¡SALUDO! -u-")
cad1="Hola"
cad2=input("Introduzca su nombre: ")
cad2=cad2.lower()
cad2=cad2.capitalize()
print("¡"+cad1+" "+cad2+"!")

#PROBLEMA 2:
print("\tCALCULADORA DE PORCENTAJE - PROPINA PARA MESERO")
costo=float(input("1. Ingrese el monto del consumo en el restaurante: "))
porcentaje=float(input("2. Ingrese el porcentaje que desea dejar de propina (en número entero): "))
propina=(porcentaje/100)*costo
print("El monto de propina que debe dejar de propina al mesero es de: "+(str(propina)))

#PROBLEMA 3:
print("\tPESO TOTAL DE UN PAQUETE")
peso_payaso=112
peso_muñeca=75
num_payasos=int(input("1. Digite el número de payasos vendidos: "))
num_muñecas=int(input("2. Digite el número de muñecas vendidas: "))
peso_caja=(peso_payaso*num_payasos)+(peso_muñeca*num_muñecas)
print("El peso del paquete será de: "+str(peso_caja)+"g.")

#PROBLEMA 4:
print("\tSUMATORIA DEL 1 AL N-ÉSIMO NÚMERO")
N=int(input("Digite un número entero positivo N: "))
if N>=0:
    sumatoria=(N*(N+1))//2
    print("La sumatoria del número 1 al " +str(N)+ " es de: " +str(sumatoria))
else:
    print("Por favor, ingrese un número entero positivo.")

#PROBLEMA 5:
print("\tSHOWS MUSICALES")
num_shows = int(input("Digite el numero de shows musicales ha visto en el último año: "))
total = num_shows>3
print("¿Ha visto más de 3 shows musicales en el último año?", total)

#PROBLEMA 6:
print("\tPRECIO DE ENTRADA DE UNA SALA DE JUEGOS.")
edad=int(input("Digite su edad: "))
if edad<4:
    entrada=0
elif 4<=edad<=18:
    entrada=5
else:
    entrada=10 
print("El precio de la entrada para usted es de " +str(entrada))

#PROBLEMA 7:
print("\tMENÚ MATEMÁTICO")
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))

print("\tMENÚ DE OPCIONES")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (primer número menos segundo número)")
print("3. Mostrar la multiplicación de los dos números")
opcion=input("Elija una opción (1/2/3): ")

if opcion=='1':
    suma=num1+num2
    print("La suma de", num1, "y", num2, "es:", suma)
elif opcion=='2':
    resta=num1-num2
    print("La resta de", numero1, "menos", numero2, "es:", resta)
elif opcion=='3':
    multiplicacion=num1*num2
    print("La multiplicación de", num1, "y", num2, "es:", multiplicacion)
else:
    print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

#PROBLEMA 8:
print("\tHORA DE COMER!")
hora=input("Ingrese la hora en formato HH:MM: ")
hora=hora.split(":")
hora=float(hora[0])+float(hora[1])/60
if 7.0<=hora<=8.0:
    print("Es la hora de desayunar.")
elif 12.0<=hora<=13.0:
    print("Es la hora de almorzar.")
elif 18.0<=hora<=19.0:
    print("Es la hora de cenar.")

#PROBLEMA 9:
print("\tLISTA INVERTIDA")
lista=['Di','buen','día','a','papá']
lista.reverse()
print(lista)

#PROBLEMA 10:
print("\tELIMINAR ELEMENTOS DE UNA LISTA")
lista= ['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
ind_eliminar=[0,4,5]
lista_resultado=[lista[i] for i in range(len(lista)) if i not in ind_eliminar]
print(lista_resultado)

#PROBLEMA 11:
print("\tELIMINAR DUPLICADOS")
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = []
print("La lista original es: ", lista_original)
for elemento in lista_original:
    if elemento not in lista_procesada:
        lista_procesada.append(elemento)

print("La lista procesada es: ", lista_procesada)

#PROBLEMA 12:
print("\tEXTENSIONES DE ARCHIVO")
nombre_archivo = input("Ingrese el nombre del archivo: ")
nombre_archivo = nombre_archivo.lower()

if nombre_archivo.endswith('.gif'):
    mime='image/gif'
elif nombre_archivo.endswith('.jpg') or nombre_archivo.endswith('.jpeg'):
    mime='image/jpeg'
elif nombre_archivo.endswith('.png'):
    mime='image/png'
elif nombre_archivo.endswith('.pdf'):
    mime='application/pdf'
elif nombre_archivo.endswith('.txt'):
    mime='text/plain'
elif nombre_archivo.endswith('.zip'):
    mime='application/zip'
else:
    mime='application/octet-stream'

print("El tipo de archivo MIME es:", mime)