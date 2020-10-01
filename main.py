game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('Hello and Welcome to Tic Tac Toe Murder')

def display_board(game_baord):
    print(str(game_baord[0]) + '|'+ str(game_baord[1]) + '|'+ str(game_baord[2]))
    print('-----')
    print(str(game_baord[3]) + '|'+ str(game_baord[4]) + '|'+ str(game_baord[5]))
    print('-----')
    print(str(game_baord[6]) + '|'+ str(game_baord[7]) + '|'+ str(game_baord[8]))

display_board(game_board)


def play_on():
  control = 1
  while control == 1:
    result_yn = input('Do you want to play a game? *SAW* (Y/N)')

    if result_yn == "Y":
      print('Okay...')
      return 'Y'
      control = 2
    
    if result_yn == 'N':
      print('Smart move')
      control = 2
      return 'N'
      break
    

y_n = play_on()

def player_input(a):
  while a == 'Y':
    result = input('Please Select  position for your next move 1-9')
    if int(result) in range(1,10):
      return int(result)
      break
    else:
      pass

selection = player_input(y_n)

def place_marker(board,marker,position):
  board[position] = marker
  return board

place_marker(game_board, 'X', selection)

display_board(game_board)