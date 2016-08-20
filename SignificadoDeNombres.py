#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Diego Caraballo
# www.pythondiario.com

# Importamos librerias necesarias
from bs4 import BeautifulSoup
import mechanize
import os

# Instanciamos el objeto br
br = mechanize.Browser()

# Opciones para el navegador
# Ingnora robots.txt
br.set_handle_robots(False)
br.set_handle_equiv(False)
# Simula ser una persona
br.addheaders = [('User-agent', 'Mozilla/5.0')] 

# Opcion para terminar el bucle
opcion = "N"

# Bucle para seguir mostrando nombres
while (opcion != "S"):
	nombre = raw_input("Ingrese un nombre: ")
	
	# Pagina web
	url = 'http://www.misabueso.com/nombres/nombre.php'

	br.open(url)   

	br.select_form(nr= 0)

	br.form[ 'nombre' ] = nombre
	print ""

	# Guardo el contenido del resultado de apretar el boton buscar en formato (html)
	data = br.submit()
	
	# Instancio el objeto soup
	soup = BeautifulSoup(data, "html.parser")

	# Busco dentro del div, donde tengo el texto del nombre
	div = soup.find_all("div", {"class" : "in_a_box"})
	
	# Cantidad de lineas
	cant = len(div)
	
	# Recorro hasta la penultima linea del div y luego muestro
	for i in div[:(cant-1)]:
		print i.text + "\n"
		
	print ""
	
	opcion	= raw_input("Presiones 'S' para Salir...")
	# Convierto la letra a Mayusculas
	opcion = opcion.upper()
	# Limpia pantalla, usar 'cls' para Windows
	os.system("clear")


