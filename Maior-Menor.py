import game_data
import arte
import lib

lib.print_art(arte.logo)
fim_jogo = False
score = 0
option_1 = lib.escolher_aleatorio(game_data.database)
while not fim_jogo:
    option_2 = lib.escolher_aleatorio(game_data.database)
    while option_1 == option_2: #impede repetição
        option_2 = lib.escolher_aleatorio(game_data.database)
    fim_jogo, temp = lib.jogar_round(option_1, option_2)
    if not fim_jogo:
        score += 1
        lib.clear()
        option_1 = temp
lib.clear()
print(f"You lost!\n"
      f" A: {option_1['name']} has {option_1['follower_count']}k followers\n"
      f" B: {option_2['name']} has {option_2['follower_count']}k followers\n"
      f"Score:{score}"
      )