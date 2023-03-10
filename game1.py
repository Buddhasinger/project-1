print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


import random

selector = 0
player_guess = 0
number = 0
player_turn = 0
cyber_player = 0


def stone_scissors_paper(player_turn, cyber_player):
    while True:
        player_turn = int(input(
            'Игра "Камень, ножницы, бумага".\nВыберите число:\n1 - КАМЕНЬ\n2 - НОЖНИЦЫ\n3 - БУМАГА\n0 - Выход в главное меню.\nВаш ход: '))
        cyber_player = random.randint(1, 3)
        # print(cyber_player, player_turn)
        print()
        if player_turn == 0:
            print('Игра закончена')
            break
        elif player_turn == cyber_player:
            if player_turn == 1:
                print('Все выбрали камень. Нужно переиграть')
            elif player_turn == 2:
                print('Все выбрали ножницы. Нужно переиграть')
            elif player_turn == 3:
                print('Все выбрали бумагу. Нужно переиграть')
            print()

        elif (player_turn == 1 and cyber_player == 2):
            print('Вы выбрали камень, а другой игрок выбрал ножницы.\nКамень бьёт ножницы. Вы выиграли!')
            print()
        elif (player_turn == 2 and cyber_player == 1):
            print('Вы выбрали ножницы, а другой игрок выбрал камень.\nКамень бьёт ножницы. Вы проиграли.')
            print()
        elif (player_turn == 2 and cyber_player == 3):
            print('Вы выбрали ножницы, а другой игрок выбрал бумагу.\nНожницы режут бумагу. Вы выиграли!')
            print()
        elif (player_turn == 3 and cyber_player == 2):
            print('Вы выбрали бумагу, а другой игрок выбрал ножницы.\nНожницы режут бумагу. Вы проиграли.')
            print()
        elif (player_turn == 3 and cyber_player == 1):
            print('Вы выбрали бумагу, а другой игрок выбрал камень.\nБумага накрывает камень. Вы выиграли!')
            print()
        elif (player_turn == 1 and cyber_player == 3):
            print('Вы выбрали камень, а другой игрок выбрал бумагу.\nБумага накрывает камень. Вы проиграли.')
            print()
        else:
            print('Ошибка ввода.')


def guess_the_number(player_guess, number):
    while True:
        player_choice = int(input('Игра "Угадай число от 0 до 100."\n1 - Угадать число\n0 - Выход в главное меню: '))
        if player_choice == 0:
            break
        elif player_choice == 1:
            number = random.randint(0, 100)
            while True:
                player_guess = int(input('Введите число: '))
                if number != player_guess:
                    if number > player_guess:
                        print('Число больше, чем Вы предположили.')
                    else:
                        print('Число меньше, чем Вы предположили.')
                else:
                    print('Вы угадали!')
                    break
            print(number)
        else:
            print('Ошибка ввода.\n1 - Угадать число/n0 - Выход в главное меню.')


def mainMenu(selector):
    while True:
        selector = int(input('Выбор игры.\n1 - Камень, ножницы, бумага.\n2 - Угадай число.\n0 - Выход.\nВаш выбор: '))
        print()
        if selector == 1:
            stone_scissors_paper(player_turn, cyber_player)
        elif selector == 2:
            guess_the_number(player_guess, number)
        elif selector == 0:
            print('Игры кончились.')
            break
        else:
            print('Ошибка ввода. Введите "1", "2" или "0" для выхода.')


mainMenu(selector)