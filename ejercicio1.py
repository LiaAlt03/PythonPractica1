'''Problema 1: Escribir un programa que solicite su nombre de usuario por consola y 
después de que el usuario lo introduzca muestre por pantalla la cadena “¡Hola <nombre>!”,
donde <nombre> es el nombre que el usuario haya introducido.
'''
print("\t¡SALUDO! -u-")
cad1="Hola"
cad2=input("Introduzca su nombre: ")
cad2=cad2.lower()
cad2=cad2.capitalize()
print("¡"+cad1+" "+cad2+"!")

'''
Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.
'''
print("\tCALCULADORA DE PORCENTAJE - PROPINA PARA MESERO")
costo=float(input("1. Ingrese el monto del consumo en el restaurante: "))
porcentaje=float(input("2. Ingrese el porcentaje que desea dejar de propina (en número entero): "))
propina=(porcentaje/100)*costo
print("El monto de propina que debe dejar de propina al mesero es de: "+(str(propina)))

'''
Problema 3:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
'''
print("\tPESO TOTAL DE UN PAQUETE")
peso_payaso=112
peso_muñeca=75
num_payasos=int(input("1. Digite el número de payasos vendidos: "))
num_muñecas=int(input("2. Digite el número de muñecas vendidas: "))
peso_caja=(peso_payaso*num_payasos)+(peso_muñeca*num_muñecas)
print("El peso del paquete será de: "+str(peso_caja)+"g.")

'''
Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N.
'''




'''
Problema 5:
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.
'''