from Drawings_Menu import drawing


def logica(idioma, palabra):

	# Inicializar variables
	vidas = 0
	numero_de_letras = len(palabra)
	letras_correctas = []
	letras_incorrectas = []

	# Mostrar espacios iniciales
	print("\n")
	for i in range(numero_de_letras):
		letras_correctas.append("_")

	# print(palabra) # Para pruebas

	# Juego
	while vidas < 6 and "_" in letras_correctas:
		letra_encontrada = False
		drawing(vidas)
		print(letras_correctas)
		let_inc(idioma, letras_incorrectas)
		letra = pedir_letra(idioma)

		for i in range(numero_de_letras):
			if letra == palabra[i]:
				letras_correctas.pop(i)
				letras_correctas.insert(i, letra)
				letra_encontrada = True

		if not letra_encontrada:
			vidas += 1
			letras_incorrectas.append(letra)
			drawing(vidas)
			print(letras_correctas)

	win_lose(idioma, vidas, palabra)


def win_lose(idioma, vidas, palabra):
	if vidas == 6:
		if idioma == 1:
			print(f"You lose, the word was: {palabra}")

		elif idioma == 2:
			print("Perdiste, la palabra era: ", palabra)
		elif idioma == 3:
			print("Tu as perdu, le mot était: ", palabra)
	else:
		if idioma == 1:
			print("You win")
			print(f"The word was: {palabra}")
		elif idioma == 2:
			print("Ganaste")
			print(f"La palabra era: {palabra}")
		elif idioma == 3:
			print("Tu as gagné")
			print(f"Le mot était: {palabra}")


def let_inc(idioma, letras_incorrectas):
	if idioma == 1:
		print(f"Incorrect letters: {letras_incorrectas}")
	elif idioma == 2:
		print(f"Letras incorrectas: {letras_incorrectas} ")
	elif idioma == 3:
		print(f"Lettres incorrectes: {letras_incorrectas} ")


def pedir_letra(idioma):
	if idioma == 1:
		letra = input("Enter a letter: ")
		return letra
	elif idioma == 2:
		letra = input("Ingresa una letra: ")
		return letra
	elif idioma == 3:
		letra = input("Entrez une lettre: ")
		return letra
