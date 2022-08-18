import os.path
from platform import architecture
from re import A
from tkinter import N
	
os.system("cls")

def cargo():

	ISBN= input("Ingrese ISBN: ").strip()
	TITULO = input("Ingrese Titulo: ").upper().strip()
	AUTOR= input("Ingrese autor: ").upper().strip()
	GENERO= input("Ingrese Genero: ").upper().strip()
	PRECIO= input("Ingrese Precio: ").strip()
	LINEA= ISBN + " ,  "+  TITULO + " , " + AUTOR + ", "  + GENERO +  "," + PRECIO + " \n"
	return LINEA

ListaISBN=[]
ListaTitulo=[]
ListaAutor= []
ListaGenero=[]
ListaPrecio=[] 
listaLibro =[ListaISBN, ListaTitulo, ListaAutor, ListaGenero, ListaPrecio] 

if os.path.isfile (" Baselibros.txt"):
 		Archivo =open("Baselibros.txt", "a")
		
else:
 	Archivo=open("Baselibros.txt", "w")



Continuar= input("Desea ingresar un libro (S/N) ->  ").upper()

while Continuar == "S": 


	ISBN= input("Ingrese ISBN: ")
	TITULO = input("Ingrese Titulo: ").upper().strip()
	AUTOR= input("Ingrese autor: ").upper().strip()
	GENERO= input("Ingrese Genero: ").upper().strip()
	PRECIO= (input("Ingrese Precio: ")).strip()

	ListaISBN.append(ISBN)
	ListaTitulo.append(TITULO)
	ListaAutor.append(AUTOR)
	ListaGenero.append(GENERO)
	ListaPrecio.append(PRECIO)

	Continuar = input("¿Desea continuar con la carga? (S/N) ->  ").upper()





print("                         MENU OPCIONES DE LIBRERIA                             \n  ")

Menu = int(input (" 1. Buscar por ISBN \n 2. Buscar por TITULO \n 3. Buscar por AUTOR \n 4. Buscar por GENERO \n 5. LISTADO GENERAL \n 6. AGREGAR LIBRO \n 0. SALIR \n \n  Ingrese una Opcion ->  "))

while Menu != "":
	

	if Menu == 1:
		BusquedaISBN = (input("Ingrese ISBN: "))
		if BusquedaISBN in ListaISBN:
			print("Resultados de la busqueda: ")
			ResultadoBusqueda = ListaISBN.index(BusquedaISBN)
			print(ListaTitulo[ResultadoBusqueda])
			print(ListaAutor[ResultadoBusqueda])
			print(ListaGenero[ResultadoBusqueda])
			print(ListaPrecio[ResultadoBusqueda])
			

			Continuar = input("¿ Desea modificar el ISBN? (S/N) ->  ").upper

			if Continuar == "S":
				NuevoISBN = input("Ingrese Nuevo ISBN: ->  ")
				for x in range(len(ListaISBN)):
					ListaISBN [x] == BusquedaISBN
					ListaISBN[x] = NuevoISBN
					print (" Se ah modificado exitosamente ")
		else:
			print("No se ha encontrado en esta busqueda: ")
			print("                         MENU OPCIONES DE LIBRERIA                             \n  ")

			Menu = int(input (" 1. Buscar por ISBN \n 2. Buscar por TITULO \n 3. Buscar por AUTOR \n 4. Buscar por GENERO \n 5. LISTADO GENERAL \n 6. AGREGAR LIBRO \n 0. SALIR-GUARDAR \n \n  Ingrese una Opcion ->  "))

			
		
	elif Menu == 2:
		
		BusquedaTITULO = input("Ingrese TITULO").upper().strip()
		if BusquedaTITULO in ListaTitulo:
			print("Resultados de la busqueda: ")
			ResultadoBusqueda = ListaTitulo.index(BusquedaTITULO)
			print(ListaTitulo[ResultadoBusqueda])
			print(ListaAutor[ResultadoBusqueda])
			print(ListaGenero[ResultadoBusqueda])
			print(ListaPrecio[ResultadoBusqueda])

			if Continuar == "S":
				NuevoTITULO = input("Ingrese Nuevo TITULO : -> ").upper()
				for x in range(len(ListaTitulo)):
					ListaTitulo [x] == ListaTitulo
					ListaTitulo [x]= NuevoTITULO
					print (" Se ah modificado exitosamente ")
		

		else:
			print("No se ha encontrado en esta busqueda: ")
			print("                         MENU OPCIONES DE LIBRERIA                             \n  ")

			Menu = int(input (" 1. Buscar por ISBN \n 2. Buscar por TITULO \n 3. Buscar por AUTOR \n 4. Buscar por GENERO \n 5. LISTADO GENERAL \n 6. AGREGAR LIBRO \n 0. SALIR-GUARDAR \n \n  Ingrese una Opcion ->  "))


	elif Menu == 3:
		
		BusquedaAUTOR = input("Ingrese AUTOR").upper().strip()
		if BusquedaAUTOR in ListaAutor:
			print("Resultados de la busqueda: ")
			ResultadoBusqueda = ListaAutor.index(BusquedaAUTOR)
			print(ListaTitulo[ResultadoBusqueda])
			print(ListaAutor[ResultadoBusqueda])
			print(ListaGenero[ResultadoBusqueda])
			print(ListaPrecio[ResultadoBusqueda])

		else:
			print("No se ah encontrado en esta busqueda: ")
			print("                         MENU OPCIONES DE LIBRERIA                             \n  ")

			Menu = int(input (" 1. Buscar por ISBN \n 2. Buscar por TITULO \n 3. Buscar por AUTOR \n 4. Buscar por GENERO \n 5. LISTADO GENERAL \n 6. AGREGAR LIBRO \n 0. SALIR-GUARDAR \n \n  Ingrese una Opcion ->  "))


	elif Menu == 4:
		BusquedaGENERO = input("Ingrese GENERO").upper().strip()
		if BusquedaGENERO in ListaGenero:
			print("Resultados de la busqueda: ")
			ResultadoBusqueda = ListaISBN.index(BusquedaGENERO)
			print(ListaTitulo[ResultadoBusqueda])
			print(ListaAutor[ResultadoBusqueda])
			print(ListaGenero[ResultadoBusqueda])
			print(ListaPrecio[ResultadoBusqueda])

		else:
			print("No se ha encontrado en esta busqueda: ")
			print("                         MENU OPCIONES DE LIBRERIA                             \n  ")

			Menu = int(input (" 1. Buscar por ISBN \n 2. Buscar por TITULO \n 3. Buscar por AUTOR \n 4. Buscar por GENERO \n 5. LISTADO GENERAL \n 6. AGREGAR LIBRO \n 0. SALIR-GUARDAR \n \n  Ingrese una Opcion ->  "))

			
	
	elif Menu == 5:
		Archivo = open("Baselibros.txt", "a")
		print(f"El LISTADO GENRAL ES, {listaLibro}{ListaTitulo} \n ".format(Archivo))
		Archivo.close()
		break
	
	elif Menu == 6:
		Archivo =open("Baselibros.txt", "a")
		CargaLibro = cargo()
		Archivo.write(CargaLibro)
		Archivo.close()
		break

	elif Menu == 0:
		##filehandle: Maneja los datos-lee y los devuelve al archivo seleccioando
		with open('Baselibros.txt', 'a') as filehandle:
			filehandle.writelines("%s" % place for place in listaLibro)
			quit()


	else:
		print("......FIN DEL PROGRAMA.......")


		#ISBN =  input("Ingrese ISBN -> ").strip()
		#TITULO = input("Titulo -> ").upper()
		#AUTOR = input("Autor -> ").upper()
		#GENERO = input("Genero -> ").upper()
		#LIBRO6 = ISBN + " ,  "+  TITULO + " , " + AUTOR + ", "  + GENERO + " \n"

		#Archivo = open("Baselibros.txt", "a")
		#Archivo.write(LIBRO6)
		#Continuar = input("Desea agregar otro libro (S/N) ->  ").upper()
		#Archivo.close()
	
	
		#while Continuar == "N":
			#print("                         MENU OPCIONES DE LIBRERIA                             \n  ")
			#Menu = int(input (" 1. Buscar por ISBN \n 2. Buscar por TITULO \n 3. Buscar por AUTOR \n 4. Buscar por GENERO \n 5. LISTADO GENERAL \n 6. AGREGAR LIBRO \n 0. SALIR-GUARDAR \n \n  Ingrese una Opcion ->  "))
