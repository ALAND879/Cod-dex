
def lang():
	print("""
	Select a language / Selecciona un idioma /  "Sélectionnez une langue"
	1. English
	2. Español
	3. Français
	""")
	idioma = int(input("Select an option: "))
	return idioma


def menu_es():
	print("""
	1. Jugar
	2. Instrucciones
	3. Cambiar idioma
	4. Salir
	""")
	juego = int(input("Selecciona una opción: "))
	return juego


def menu_en():
	print("""
	1. Play
	2. Instructions
	3. Change language
	4. Exit
	""")
	juego = int(input("Select an option: "))
	return juego


def menu_fr():
	print("""
	1. Jouer
	2. Instructions
	3. Changer de langue
	4. Quitter
	""")
	juego = int(input("Sélectionnez une option: "))
	return juego


def menu(number):
	if number == 1:
		juego = menu_en()
		return juego
	elif number == 2:
		juego = menu_es()
		return juego
	elif number == 3:
		juego = menu_fr()
		return juego


def category_es():
	print("""
	Selecciona una categoría:
	1. Animales
	2. Comida
	3. Países
	4. Profesiones
	5. Personalizado
	""")
	categoria = int(input("Selecciona una opción: "))
	return categoria


def category_en():
	print("""
	Select a category:
	1. Animals
	2. Food
	3. Countries
	4. Professions
	5. Custom
	""")
	categoria = int(input("Select an option: "))
	return categoria


def category_fr():
	print("""
	Sélectionnez une catégorie:
	1. Animaux
	2. Nourriture
	3. Pays
	4. Professions
	5. Personnalisé
	""")
	categoria = int(input("Sélectionnez une option: "))
	return categoria


def category(number):
	if number == 1:
		categoria = category_en()
		return categoria
	elif number == 2:
		categoria = category_es()
		return categoria
	elif number == 3:
		categoria = category_fr()
		return categoria


# Select language
def select_idioma():
	a = 1
	while a == 1:
		idioma = lang()
		if idioma == 1 or idioma == 2 or idioma == 3:
			a += 1
			return idioma
		else:
			print("Select a valid option")

def select_category(idioma):
	a = 1
	while a == 1:
		categoria = category(idioma)
		if categoria == 1 or categoria == 2 or categoria == 3 or categoria == 4 or categoria == 5:
			a += 1
			return categoria
		else:
			print("Select a valid option")

def drawing(number):
	hangman = ['''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''', '''
     +---+
     |   |
     😶  |
         |
         |
         |
    =========
    ''', '''
     +---+
     |   |
     😐  |
     |   |
         |
         |
    =========
    ''', '''
     +---+
     |   |
     😦  |
    /|   |
         |
         |
    =========
    ''', '''
     +---+
     |   |
     😨  |
    /|\\  |
         |
         |
    =========
    ''', '''
     +---+
     |   |
     😰  |
    /|\\  |
    /    |
         |
    =========
    ''', '''
     +---+
     |   |
     😵  |
    /|\\  |
    / \\  |
         |
    =========
    '''
	]

	print(hangman[number])
