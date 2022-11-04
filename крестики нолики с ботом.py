import random


def greetings():
    print('  Суперигра в крестики нолики с ботом! v1.0  ')
    print('  Бот играет за нолик, интеллекта столько же ')
    print('Не ставит О когда надо выиграть или помешать ')
    print('выиграть игроку, если кто знает как исправить')
    print('буду благодарен                              ')
    print('*********************************************')
    print('          Чтобы поставить Х или О            ')
    print('         введите х - номер строки            ')
    print('         введите у - номер столбца           ')


field = [[" "] * 3 for i in range(3)]


def board():
    print()
    print(f'  0 1 2')
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")


def check_input():
    while True:
        if count % 2 == 1:
            print('Ход крестика')
            coord = input('Ваш ход: ').split()
            if len(coord) != 2:
                print('Ошибка, введите 2 координаты ')
                continue

            x, y = coord
            if not (x.isdigit()) or not (y.isdigit()):
                print('Ошибка, нужно ввести числа ')
                continue

            x, y = int(x), int(y)
            if x < 0 or x > 2 or 0 > y or y > 2:
                print('Ошибка, координаты не могут быть меньше 0 и больше 2 ')
                continue

            if field[x][y] != ' ':
                print('Ошибка, клетка занята ')
                continue

            return x, y
        if count % 2 == 0:
            print('Ход нолика')
            x, y = random.choice([0, 1, 2]), random.choice([0, 1, 2])
            if field[x][y] != ' ':
                print('Ошибка, клетка занята ')
                continue
            return x, y


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        x_or_y = []
        for c in coord:
            x_or_y.append(field[c[0]][c[1]])
        if x_or_y == ['X', 'X', 'X']:
            board()
            print('Победил крестик, честь и хвала ему')
            return True
        if x_or_y == ['O', 'O', 'O']:
            board()
            print('Победил нолик, честь и хвала ему')
            return True
    return False


greetings()
count = 0
while True:
    count += 1
    board()
    x, y = check_input()
    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'
    if check_win():
        break
    if count == 9:
        print('Ничья, победила дружба')
        break
