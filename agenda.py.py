

import email
import os
import pathlib

#Creando Variables
Salir=0
Agregar=1
Mostrar=2
Buscar=3

def mostrarMenu():
    os.system("cls")#No es necesario generarla pero hace que la aplicación sea mas rapida
    print(f""" Bienvenido a tú Mega Agenda 
            {Agregar}) Insertar Contacto
            {Mostrar}) Mostrando Contacto
            {Buscar})  Buscar Contacto
            {Salir})  Saliendo de Agenda"""
            )

def CrearAgenda(agenda,nombreArchivo):
    if pathlib.Path(nombreArchivo,"r").exists(): #r abreviatura de read, para leer el archivo
        with open(nombreArchivo) as archivo: # renombrando archivo
            for linea in archivo: #Recorriendo las lineas del archivo
                Contacto, telefono, correo = linea.strip().split(",")
                agenda.setdefault(Contacto,(telefono, correo))
    else:
         with open(nombreArchivo,"w") as archivo: # renombrando archivo
            pass #esta funcion nos permite pasar de una función a otra, cuando no queramos colocar mas codigo

def agregarContacto(agenda,nombreArchivo):
    os.system("cls")
    print("Agregar Contacto")
    Nombre= input("Indicar nombre del contacto: ")
    if agenda.get(Nombre):
        print("El contacto ya esta dentro de la agenda")
    else:
        telefono= input("Indicar telefono del contacto: ")
        correo= input("Indicar correo del contacto: ")
        agenda.setdefault(Nombre,(telefono, correo))
        with open(nombreArchivo,"a") as archivo: # a es para (add) añadir
            archivo.write (f'{Nombre}, {telefono}, {correo} \n')
        print("Contacto se agrego con exito")

def mostrarContacto(agenda): #es para mostrar todos
    os.system("cls")
    print("Mostrar Contacto")
    if len(agenda)>0:
        for contacto, datos in agenda.items():
            print(f'Nombre del contacto : {contacto}')
            print(f'Telefono del contacto : {datos[0]}')
            print(f'Correo del contacto : {datos[1]}')
    else:
        print("No hay ningún contacto registrado en la agenda")

def buscarContacto(agenda): #solo busca uno 
    os.system("cls")
    print("Buscar Contacto")
    if len(agenda)>0:
        Nombre= input("Buscar el contacto: ")
        coincidencias=0
        for contacto, datos in agenda.items():
            if Nombre in contacto:
                print(f'Nombre del contacto : {contacto}')
                print(f'Telefono del contacto : {datos[0]}')
                print(f'Correo del contacto : {datos[1]}')
                coincidencias+=1
                print('#'*30) #es solo para que quede bien, es estetica
        if coincidencias==0:
            print("No se encontro el contacto")
        else:
            print(f'Se encontraron la cantidad de  {coincidencias} contactos')
    else:
        print("No hay ningún contacto registrado en la agenda")

def main():
    continuar=True
    agenda=dict() #nos sirve para el llamado de archivo externos"
    nombreArchivo="LaAgenda.txt"
    CrearAgenda(agenda,nombreArchivo)
    while continuar:
        mostrarMenu()
        opcion= int(input("Por favor, selecciona una opción "))
        if opcion==Agregar:
            agregarContacto(agenda,nombreArchivo)
        elif opcion==Mostrar:
            mostrarContacto(agenda)
        elif opcion==Buscar:
            buscarContacto(agenda)
        elif opcion==Salir:
            continuar=False
        else:
            print("La opción ingresada no es valida")
        input("Presiona enter para continuar")

if __name__=="__main__":
    main()