# Comida, Animales, Paises, Profesiones
# Inglés, Español y Frances
from random import choice
#  Comida

Comida_Esp = ['Tacos', 'Enchiladas', 'Chiles Rellenos', 'Pozole', 'Tamales', 'Guacamole', 'Churros', 'Flan', 'Ceviche', 'Mole', 'Carnitas', 'Chiles en Nogada', 'Menudo', 'Pambazo',
              'Sopes', 'Tostadas', 'Quesadillas', 'Empanadas', 'Chalupas', 'Molletes', 'Huevos Rancheros', 'Chilaquiles', 'Torta Ahogada', 'Barbacoa', 'Birria', 'Cochinita Pibil',
              'Pozole', 'Tamal', 'Pulque', 'Mezcal', 'Tequila', 'Horchata', 'Tlayudas', 'Champurrado', 'Atole', 'Pico de Gallo', 'Salsa Verde', 'Salsa Roja', 'Margarita',
              'Michelada', 'Cerveza', 'Tepache', 'Café de Olla', 'Pan de Muerto', 'Rosca de Reyes', 'Buñuelos', 'Cajeta', 'Mazapán', 'Tejocote', 'Rompopes']

Comida_Eng = ['Fish and Chips', 'Roast Beef', 'Yorkshire Pudding', 'Cornish Pasty', 'Full English Breakfast', 'Shepherd’s Pie', 'Black Pudding', 'Ploughman’s Lunch',
              'Bangers and Mash', 'Toad in the Hole', 'Eton Mess', 'Sticky Toffee Pudding', 'Bakewell Tart', 'Victoria Sponge', 'Scones', 'Crumpets', 'Mince Pies',
              'Christmas Pudding', 'Bread and Butter Pudding', 'Trifle', 'Apple Crumble', 'Custard', 'Cream Tea', 'English Muffin', 'Scotch Egg', 'Pork Pie',
              'Chicken Tikka Masala', 'Beef Wellington', 'Lancashire Hotpot', 'Corned Beef Hash', 'Bubble and Squeak', 'Spotted Dick', 'Jellied Eels', 'Cottage Pie',
              'Liver and Onions', 'Gammon Steak', 'Welsh Rarebit', 'Eccles Cake', 'Banoffee Pie', 'Knickerbocker Glory', 'Summer Pudding', 'Rhubarb Crumble', 'Lemon Drizzle Cake',
              'Chicken and Leek Pie', 'Steak and Kidney Pie', 'Chicken and Mushroom Pie', 'Beef and Ale Pie', 'Pork and Apple Pie', 'Lamb and Mint Pie', 'Huntingdon Fidget Pie',
              'Bedfordshire Clanger', 'Melton Mowbray Pork Pie', 'Stargazy Pie', 'Sussex Pond Pudding', 'Bakewell Pudding', 'Treacle Tart', 'Jam Roly-Poly']

Comida_Fr = ['Ratatouille', 'Coq au Vin', 'Bouillabaisse', 'Quiche Lorraine', 'Croissant', 'Baguette', 'Pain au Chocolat', 'Tarte Tatin', 'Crème Brûlée', 'Macarons', 'Éclair',
             'Profiterole', 'Madeleines', 'Pain Perdu', 'Tarte Flambée', 'Chateaubriand', 'Pot-au-Feu', 'Cassoulet', 'Escargots de Bourgogne', 'Foie Gras', 'Raclette',
             'Tartiflette', 'Bœuf Bourguignon', 'Soupe à l’Oignon', 'Poulet de Bresse', 'Canard à l’Orange', 'Salade Niçoise', 'Pissaladière', 'Rillettes', 'Pâté', 'Quenelles',
             'Gougères', 'Baba au Rhum', 'Mille-Feuille', 'Tarte au Citron Meringuée', 'Crêpes', 'Galette', 'Canelé', 'Clafoutis', 'Far Breton', 'Kouign-Amann', 'Tarte Normande',
             'Calvados', 'Camembert', 'Roquefort', 'Brie de Meaux', 'Comté', 'Reblochon', 'Munster', 'Époisses', 'Bleu d’Auvergne', 'Crottin de Chavignol', 'Saint-Nectaire',
             'Tomme de Savoie', 'Pont-l’Évêque', 'Livarot', 'Maroilles', 'Morbier', 'Ossau-Iraty', 'Fourme d’Ambert', 'Langres', 'Chaource', 'Neufchâtel']

# Animales

Animales_Esp = ['Perro', 'Gato', 'Elefante', 'León', 'Tigre', 'Oso', 'Jirafa', 'Cebra', 'Mono', 'Lobo', 'Zorro', 'Conejo', 'Ratón', 'Ardilla', 'Pájaro', 'Pez', 'Tortuga',
                'Serpiente', 'Rana', 'Cocodrilo', 'Caballo', 'Vaca', 'Cerdo', 'Pato', 'Gallina', 'Pavo', 'Búho', 'Águila', 'Foca', 'Pingüino', 'Canguro', 'Koala', 'Hipopótamo',
                'Rinoceronte', 'Camello', 'Delfín', 'Ballena', 'Murciélago', 'Mariposa', 'Abeja', 'Mosquito', 'Cucaracha', 'Araña', 'Ciempiés', 'Escorpión', 'Cangrejo', 'Langosta',
                'Pulpo', 'Medusa', 'Estrella de mar']

Animales_Eng = ['Dog', 'Cat', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Zebra', 'Monkey', 'Wolf', 'Fox', 'Rabbit', 'Mouse', 'Squirrel', 'Bird', 'Fish', 'Turtle', 'Snake',
                'Frog', 'Crocodile', 'Horse', 'Cow', 'Pig', 'Duck', 'Chicken', 'Turkey', 'Owl', 'Eagle', 'Seal', 'Penguin', 'Kangaroo', 'Koala', 'Hippopotamus', 'Rhinoceros',
                'Camel', 'Dolphin', 'Whale', 'Bat', 'Butterfly', 'Bee', 'Mosquito', 'Cockroach', 'Spider', 'Centipede', 'Scorpion', 'Crab', 'Lobster', 'Octopus', 'Jellyfish',
                'Starfish']

Animales_Fr = ['Chien', 'Chat', 'Éléphant', 'Lion', 'Tigre', 'Ours', 'Girafe', 'Zèbre', 'Singe', 'Loup', 'Renard', 'Lapin', 'Souris', 'Écureuil', 'Oiseau', 'Poisson', 'Tortue',
               'Serpent', 'Grenouille', 'Crocodile', 'Cheval', 'Vache', 'Cochon', 'Canard', 'Poulet', 'Dinde', 'Hibou', 'Aigle', 'Phoque', 'Pingouin', 'Kangourou', 'Koala',
               'Hippopotame', 'Rhinocéros', 'Chameau', 'Dauphin', 'Baleine', 'Chauve-souris', 'Papillon', 'Abeille', 'Moustique', 'Cafard', 'Araignée', 'Mille-pattes', 'Scorpion',
               'Crabe', 'Homard', 'Poulpe', 'Méduse', 'Étoile de mer']

# Profesiones

Prof_Esp = ['Ingeniero', 'Médico', 'Abogado', 'Profesor', 'Arquitecto', 'Dentista', 'Farmacéutico', 'Psicólogo', 'Veterinario', 'Policía', 'Bombero', 'Carpintero', 'Pintor',
            'Electricista', 'Plomero', 'Cocinero', 'Panadero', 'Cajero', 'Camarero', 'Peluquero', 'Periodista', 'Fotógrafo', 'Actor', 'Músico', 'Bailarín', 'Escritor', 'Piloto',
            'Marinero', 'Soldado', 'Astronauta', 'Científico', 'Investigador', 'Programador', 'Diseñador', 'Jardinero', 'Mecánico', 'Taxista', 'Enfermero', 'Farmacéutico',
            'Cirujano', 'Pediatra', 'Dermatólogo', 'Cardiólogo', 'Neurólogo', 'Ginecólogo', 'Oftalmólogo', 'Ortodoncista', 'Anestesiólogo', 'Radiólogo', 'Patólogo',
            'Endocrinólogo', 'Gastroenterólogo', 'Nefrólogo', 'Reumatólogo', 'Urologista']

Prof_Eng = ['Engineer', 'Doctor', 'Lawyer', 'Teacher', 'Architect', 'Dentist', 'Pharmacist', 'Psychologist', 'Veterinarian', 'Police Officer', 'Firefighter', 'Carpenter',
            'Painter', 'Electrician', 'Plumber', 'Chef', 'Baker', 'Cashier', 'Waiter', 'Hairdresser', 'Journalist', 'Photographer', 'Actor', 'Musician', 'Dancer', 'Writer',
            'Pilot', 'Sailor', 'Soldier', 'Astronaut', 'Scientist', 'Researcher', 'Programmer', 'Designer', 'Gardener', 'Mechanic', 'Taxi Driver', 'Nurse', 'Pharmacist',
            'Surgeon', 'Pediatrician', 'Dermatologist', 'Cardiologist', 'Neurologist', 'Gynecologist', 'Ophthalmologist', 'Orthodontist', 'Anesthesiologist', 'Radiologist',
            'Pathologist', 'Endocrinologist', 'Gastroenterologist', 'Nephrologist', 'Rheumatologist', 'Urologist']

Prof_Fr = ['Ingénieur', 'Médecin', 'Avocat', 'Professeur', 'Architecte', 'Dentiste', 'Pharmacien', 'Psychologue', 'Vétérinaire', 'Policier', 'Pompier', 'Charpentier', 'Peintre',
           'Électricien', 'Plombier', 'Chef', 'Boulanger', 'Caissier', 'Serveur', 'Coiffeur', 'Journaliste', 'Photographe', 'Acteur', 'Musicien', 'Danseur', 'Écrivain', 'Pilote',
           'Marin', 'Soldat', 'Astronaute', 'Scientifique', 'Chercheur', 'Programmeur', 'Designer', 'Jardinier', 'Mécanicien', 'Chauffeur de taxi', 'Infirmier', 'Pharmacien',
           'Chirurgien', 'Pédiatre', 'Dermatologue', 'Cardiologue', 'Neurologue', 'Gynécologue', 'Ophtalmologue', 'Orthodontiste', 'Anesthésiste', 'Radiologue', 'Pathologiste',
           'Endocrinologue', 'Gastroentérologue', 'Néphrologue', 'Rhumatologue', 'Urologue']

# Países

Paises_Esp = ['España', 'México', 'Colombia', 'Argentina', 'Perú', 'Venezuela', 'Chile', 'Ecuador', 'Guatemala', 'Cuba', 'Bolivia', 'República Dominicana', 'Honduras', 'Paraguay',
              'El Salvador', 'Nicaragua', 'Costa Rica', 'Puerto Rico', 'Panamá', 'Uruguay', 'Equatorial Guinea', 'Alemania', 'Austria', 'Bélgica', 'Bulgaria', 'Chipre', 'Croacia',
              'Dinamarca', 'Eslovaquia', 'Eslovenia', 'Estonia', 'Finlandia', 'Francia', 'Grecia', 'Hungría', 'Irlanda', 'Italia', 'Letonia', 'Lituania', 'Luxemburgo', 'Malta',
              'Países Bajos', 'Polonia', 'Portugal', 'Reino Unido', 'República Checa', 'Rumanía', 'Suecia']

Paises_Eng = ['Spain', 'Mexico', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Ecuador', 'Guatemala', 'Cuba', 'Bolivia', 'Dominican Republic', 'Honduras', 'Paraguay',
              'El Salvador', 'Nicaragua', 'Costa Rica', 'Puerto Rico', 'Panama', 'Uruguay', 'Equatorial Guinea', 'Germany', 'Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Croatia',
              'Denmark', 'Slovakia', 'Slovenia', 'Estonia', 'Finland', 'France', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta',
              'Netherlands', 'Poland', 'Portugal', 'United Kingdom', 'Czech Republic', 'Romania', 'Sweden']

Paises_Fr = ['Espagne', 'Mexique', 'Colombie', 'Argentine', 'Pérou', 'Venezuela', 'Chili', 'Équateur', 'Guatemala', 'Cuba', 'Bolivie', 'République Dominicaine',
             'Honduras', 'Paraguay', 'El Salvador', 'Nicaragua', 'Costa Rica', 'Porto Rico', 'Panama', 'Uruguay', 'Guinée Équatoriale', 'Allemagne', 'Autriche', 'Belgique',
             'Bulgarie', 'Chypre', 'Croatie', 'Danemark', 'Slovaquie', 'Slovénie', 'Estonie', 'Finlande', 'France', 'Grèce', 'Hongrie', 'Irlande', 'Italie', 'Lettonie',
             'Lituanie', 'Luxembourg', 'Malte', 'Pays-Bas', 'Pologne', 'Portugal', 'Royaume-Uni', 'République Tchèque', 'Roumanie', 'Suède']

# Personalizado

Palabras_Personalizadas = []

# Instrucciones

Inst_Esp = """
    Instrucciones:
    - El juego consiste en adivinar la palabra oculta.
    - Tienes 6 oportunidades para adivinar la palabra.
    - Si adivinas la palabra, ganas el juego.
    - Si no adivinas la palabra, pierdes el juego.
    - Tienes 5 categorías para elegir: Comida, Animales, Profesiones, Paises y un modo Personalizado.
    - Los caracteres especiales son válidos dependiendo el idioma.
    
    Buena suerte!!!
    """

Inst_Eng = """
    Instructions:
    - The game consists of guessing the hidden word.
    - You have 6 opportunities to guess the word.
    - If you guess the word, you win the game.
    - If you don't guess the word, you lose the game.
    - You have 5 categories to choose from: Food, Animals, Professions, Countries and a Custom mode.
    - Special characters are valid depending on the language.
    
    Good luck!!!
    """

Inst_Fr = """
    Instructions:
    - Le jeu consiste à deviner le mot caché.
    - Vous avez 6 chances de deviner le mot.
    - Si vous devinez le mot, vous gagnez le jeu.
    - Si vous ne devinez pas le mot, vous perdez le jeu.
    - Vous avez 5 catégories à choisir: Nourriture, Animaux, Professions, Pays et un mode personnalisé.
    - Les caractères spéciaux sont valides selon la langue.
    
    Bonne chance!!!
    """


def instructions(num):
    if num == 1:
        print(Inst_Eng)
    elif num == 2:
        print(Inst_Esp)
    elif num == 3:
        print(Inst_Fr)


def llenar_palabras(palabra, idioma):
    Palabras_Personalizadas.append(palabra)
    if idioma == 1:
        print("The word has been saved correctly")
    elif idioma == 2:
        print("La palabra se ha guardado correctamente")
    elif idioma == 3:
        print("Le mot a été enregistré correctement")


def mensaje(idioma):
    if idioma == 1:
        print("A random word has been selected")
    elif idioma == 2:
        print("Se ha seleccionado una palabra al azar")
    elif idioma == 3:
        print("Un mot aléatoire a été sélectionné")


def llenado(idioma):
    a = 1
    while a == 1:
        palabra = ingresa(idioma)
        llenar_palabras(palabra, idioma)
        maspal = mas_pal(idioma)
        if maspal == 2:
            a += 1
    palabra = seleccionar_pal_random(5, idioma)
    mensaje(idioma)
    return palabra


def ingresa(idioma):
    if idioma == 1:
        palabra = input("Enter the word:")
        return palabra
    elif idioma == 2:
        palabra = input("Ingresa la palabra:")
        return palabra
    elif idioma == 3:
        palabra = input("Entrez le mot:")
        return palabra


def mas_pal(idioma):
    a = 1
    while a == 1:
        if idioma == 1:
            maspal = int(input("Do you want to enter more words? \n1)Yes \n2)No \nEnter an option:"))
            if maspal == 1 or maspal == 2:
                a += 1
                return maspal
            else:
                print("Select a valid option")
        elif idioma == 2:
            maspal = int(input("Deseas ingresar mas palabras? \n1)Si \n2)No \nIngresa una opción: "))
            if maspal == 1 or maspal == 2:
                a += 1
                return maspal
            else:
                print("Selecciona una opción válida")
        elif idioma == 3:
            maspal = int(input("Voulez-vous entrer plus de mots? \n1)Oui \n2)Non \nEntrez une option: "))
            if maspal == 1 or maspal == 2:
                a += 1
                return maspal
            else:
                print("Sélectionnez une option valide")


def seleccionar_pal_random(categoria, idioma):
    if idioma == 1:
        if categoria == 1:
            palabra = choice(Animales_Eng)
            return palabra

        elif categoria == 2:
            palabra = choice(Comida_Eng)
            return palabra

        elif categoria == 3:
            palabra = choice(Paises_Eng)
            return palabra

        elif categoria == 4:
            palabra = choice(Prof_Eng)
            return palabra

        elif categoria == 5:
            palabra = choice(Palabras_Personalizadas)
            return palabra

        else:
            print("An error occurred")

    elif idioma == 2:
        if categoria == 1:
            palabra = choice(Animales_Esp)
            return palabra

        elif categoria == 2:
            palabra = choice(Comida_Esp)
            return palabra

        elif categoria == 3:
            palabra = choice(Paises_Esp)
            return palabra

        elif categoria == 4:
            palabra = choice(Prof_Esp)
            return palabra

        elif categoria == 5:
            palabra = choice(Palabras_Personalizadas)
            return palabra

        else:
            print("Ha ocurrido un error")

    elif idioma == 3:
        if categoria == 1:
            palabra = choice(Animales_Fr)
            return palabra

        elif categoria == 2:
            palabra = choice(Comida_Fr)
            return palabra

        elif categoria == 3:
            palabra = choice(Paises_Fr)
            return palabra

        elif categoria == 4:
            palabra = choice(Prof_Fr)
            return palabra

        elif categoria == 5:
            palabra = choice(Palabras_Personalizadas)
            return palabra

        else:
            print("Une erreur s'est produite")
