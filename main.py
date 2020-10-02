game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('Hello and Welcome to Tic Tac Toe')

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
      exit(0)
      return 'N'
      break
    

y_n = play_on()

def player_input(a):
  while a == 'Y':
    result = input('Please Select  position for your next move 1-9:____')
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

def win_check(game_board,marker):
  if game_board[0] == marker and game_board[1] == marker and game_board[2] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[0] == marker and game_board[3] == marker and game_board[6] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[0] == marker and game_board[4] == marker and game_board[8] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[1] == marker and game_board[4] == marker and game_board[7] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[2] == marker and game_board[5] == marker and game_board[8] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[2] == marker and game_board[4] == marker and game_board[6] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[3] == marker and game_board[4] == marker and game_board[5] == marker:
    print(f'Winner! {marker} Wins it!')
  if game_board[6] == marker and game_board[7] == marker and game_board[8] == marker:
    print(f'Winner! {marker} Wins it!')

win_check(game_board, 'X')

def space_check(game_board, space):
  if game_board[space] == ' ':
    return True
  else:
    return False

space_check(game_board, 4)

def full_check(board):
  for item in board:
    if item == ' ':
      return False
    