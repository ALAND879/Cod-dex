# Version: 1.0
# Made by Alan David Jiménez Rodríguez
import Drawings_Menu as dm
import Game_logic as gl
import Words

def jugar():
	# Welcome message
	print("Welcome to Hangman")
	# Choose language
	idioma = dm.select_idioma()

	seguir = True
	while seguir:
		# Select menu, print it and choose an option 1)Jugar  2)Instrucciones 3)Salir
		juego = dm.menu(idioma)

		# Select option Play
		if juego == 1:
			# Select category
			categoria = dm.select_category(idioma)

			# Personalized
			if categoria == 5:
				palabra = Words.llenado(idioma)

			# Predefined
			else:
				palabra = Words.seleccionar_pal_random(categoria, idioma)

			# Play
			gl.logica(idioma, palabra)

		# Instructions
		elif juego == 2:
			# Instructions
			Words.instructions(idioma)

		# Change language
		elif juego == 3:
			# Change language
			idioma = dm.select_idioma()

		# Exit
		elif juego == 4:
			# Exit
			if idioma == 1:
				print("Goodbye")
			elif idioma == 2:
				print("Adiós")
			elif idioma == 3:
				print("Au revoir")
			break

		# Invalid option
		else:
			# Invalid option
			if idioma == 1:
				print("Select a valid option")
			elif idioma == 2:
				print("Selecciona una opción válida")
			elif idioma == 3:
				print("Sélectionnez une option valide")


jugar()

# Falta: Menu, sistema de juego
# Palabras y Dibujos listos
