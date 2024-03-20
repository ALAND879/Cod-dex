

def draw_vs_player_one(player_one_attacked, boats_hit_p1):
	print('a')


def draw_vs_player_two(player_two_attacked, boats_hit_p2):
	print('a')


def draw_one_player(player_one_attacked, boats_hit_p1):
	print('a')


player_one_board = []

player_two_board = []

IA_board = []


def fill_p1_board(dificultad):
	tablero = 1

	if dificultad == 1:
		tablero = 5
	elif dificultad == 2:
		tablero = 8
	elif dificultad == 3:
		tablero = 12

	for i in range(tablero):
		for j in range(tablero):
			player_one_board.append('_')


