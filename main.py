game_board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def display_board(game_baord):
    print(str(game_baord[0]) + '|'+ str(game_baord[1]) + '|'+ str(game_baord[2]))
    print('-----')
    print(str(game_baord[0]) + '|'+ str(game_baord[1]) + '|'+ str(game_baord[2]))
    print('-----')
    print(str(game_baord[0]) + '|'+ str(game_baord[1]) + '|'+ str(game_baord[2]))

display_board(game_board)


def play_on():
  control = 1
  while control == 1:
    result_yn = input('Do you want to play a game? *SAW* (Y/N)')

    if result_yn == "Y":
      print('Okay ghost')
      print('function here that starts game?')
      control = 2
    
    if result_yn == 'N':
      print('Smart move')
      control = 2
      break
    
play_on()
