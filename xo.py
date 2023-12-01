# import random

# board = [str(i) for i in range(1, 10)]
# player, computer = '', ''

# moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
# winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
# tab = range(1, 10)

# def print_board():
#     for i, char in enumerate(board, 1):
#         end = ' | ' if i % 3 != 0 else '\n'
#         end = '---------\n' if i != 1 else end
#         print(char if char in ('X', 'O') else i, end=end)

# def select_char():
#     return random.sample(('X', 'O'), 2)

# def can_move(move):
#     return 1 <= move <= 9 and board[move-1] == str(move)

# def can_win(player, move):
#     places = [i for i, x in enumerate(board) if x == player]
#     return any(all(ix in places for ix in tup) for tup in winners)

# def make_move(player, move, undo=False):
#     if can_move(move):
#         board[move-1] = player
#         win = can_win(player, move)
#         if undo:
#             board[move-1] = str(move)
#         return True, win
#     return False, False

# def computer_move():
#     for i in range(1, 10):
#         if make_move(computer, i, True)[1]:
#             return make_move(computer, i)
#     for i in range(1, 10):
#         if make_move(player, i, True)[1]:
#             return make_move(computer, i)
#     for tup in moves:
#         for mv in tup:
#             if can_move(mv):
#                 return make_move(computer, mv)

# def space_exist():
#     return any(x.isdigit() for x in board)

# player, computer = select_char()
# print(f'Игрок - это [{player}] and computer is [{computer}]')

# result = '%%% Deuce ! %%%'

# while space_exist():
#     print_board()
#     print('#Сделайте свой ход! [1-9] : ', end='')
#     move = int(input())
#     moved, won = make_move(player, move)
    
#     if not moved:
#         print(' >> Неверный номер! Попробуйте еще раз! ')
#         continue
#     7
#     if won:
#         result = '*** Поздравляем! Вы выиграли! ***'
#         break
#     elif computer_move()[1]:
#         result = '=== Вы проиграли ! =='
#         break

# print_board()
# print(result)


#----------------------------------------------------------------------------


import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("На данный момент нет высших баллов, они ваши!")
    else:
        print(f"Текущий высший балл - {min(attempts_list)} попыток")

def start_game():
    random_number = random.randint(1, 10)
    print("Привет, путешественник! Добро пожаловать в игру 'Угадай число'!")

    player_name = input("Как вас зовут? ")
    wanna_play = input(f"Привет, {player_name}, хотите сыграть в игру 'Угадай число'? (Введите Yes/No) ")

    attempts = 0
    show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Выберите число от 1 до 10: "))

            if guess < 1 or guess > 10:
                raise ValueError("Угадайте число в заданном диапазоне")

            if guess == random_number:
                print("Молодец! Вы угадали!")
                attempts += 1
                attempts_list.append(attempts)
                print(f"Это заняло у вас {attempts} попыток")

                play_again = input("Хотели бы вы сыграть еще раз? (Введите Yes/No): ")
                attempts = 0
                show_score()
                random_number = random.randint(1, 10)

                if play_again.lower() == "no":
                    print("Это круто, удачи!")
                    break
            elif guess > random_number:
                print("Это меньше")
                attempts += 1
            elif guess < random_number:
                print("Это больше")
                attempts += 1

        except ValueError as err:
            print(f"О нет! Это не правильное значение. Попробуйте еще раз... ({err})")

    else:
        print("Это круто, удачи!")

if __name__ == '__main__':
    start_game()
