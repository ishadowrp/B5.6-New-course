#Подключаем библиотеку генератора случайных значений
import random

#Функция которая начинает игру.
def start_game():
    print('Привет! Это игра крестики-нолики!')
    ans = input('Поиграем? (Y/N): ')
    if ans.upper() == 'Y':
        start_new_game()
    else:
        print('Пока! Поиграем в следующий раз!')

def start_new_game():
    #Инициализируем игровую доску
    desk = init_desk()
    #Выводим первый раз чистую игровую доску
    show_desk(desk)
    ans = input('Вы будете ходить первым (играть крестиками)? (Y/N): ')
    # Вызовем функцию, которая будет делать ход либо за игрока, либо за программу, в зависимости от того кого игрок выбрал для первого хода
    if ans.upper() == 'Y':
        symbolPlayer = 'X'
        symbolProgram = 'O'
        turn = make_move(desk, symbolPlayer,'player',True)
    else:
        symbolPlayer = '0'
        symbolProgram = 'X'
        turn = make_move(desk, symbolProgram,'program',True)
        show_desk(desk)

    #Создаем цикл для очередных ходов игрока и программы, по условию пока кто-то не выиграл
    while check_desk(desk):
        if turn == 'player':
            turn = make_move(desk, symbolPlayer,'player')
        else:
            turn = make_move(desk, symbolProgram,'program')
        show_desk(desk)
    #Если мы вышли из цикла значит кто-то победил. Покажем игровую доску и поздравим победителя.
    print('Игра окончена!')
    show_desk(desk)

    whoisWin = check_whois_win(desk)

    if whoisWin == 'X':
        print('Крестики выиграли!')
    elif whoisWin == 'O':
        print('Нолики выиграли!')
    else:
        print('Ничья!')

    newStart = input('Сыграем еще раз? (Y/N): ')
    if newStart.upper() == "Y":
        start_game()
    else:
        print('До свидания!')

# Функция которая будет выполнять ход за игрока или программу
def make_move(desk, symbol, t, firstMove = False):
    if t == 'player':
        print('Ваш ход!')
        x = int(input('Введите координату на игровой доске по Оси X: '))
        y = int(input('Введите координату на игровой доске по Оси Y: '))
        while desk[x-1][y-1] != "-":
            print('Вы выбрали уже заполенную ячейку! Укажите другие координаты!')
            x = int(input('Введите координату на игровой доске по Оси X: '))
            y = int(input('Введите координату на игровой доске по Оси Y: '))

        desk[x-1][y-1] = symbol
        return 'program'
    else:
        print('Ход компьюетра!')
        # если это первый ход у компьютера, то ставим крестик в центральную ячейку.
        if firstMove:
            x = 1
            y = 1
            desk[x][y] = symbol
        else:
            #Делаем ход за компьютер в цикле, для того чтоб проверить, что ход компьютером будет сделан в свободную ячейку
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            while desk[x-1][y-1] != "-":
                x = random.randint(1,3)
                y = random.randint(1,3)

            desk[x - 1][y - 1] = symbol
        return 'player'

#Функция проверки закончена игра или нет. Возвращает Ложь если игра закончена и Истину, если игру нужно продалжать
def check_desk(desk):

    #Проверим есть ли победитель
    win = check_whois_win(desk)
    if win != 'noOne':
        return False

    #Если победитель не определен значение: noOne, тогда проверим есть ли свободные ячейки и если их нет, то признаем ничью
    withdraw = True
    for x in range(3):
        for y in range(3):
            if desk[x][y] == '-':
                #если нашли хоть одну свободную ячейку, то игра продолжается
                withdraw = False
                break

    if withdraw == True:
        return False
    else:
        return True

# Определим есть ли победитель
def check_whois_win(desk):
    #Условия для крестиков
    if (desk[0][0] == 'X' and desk[0][1] == 'X' and desk[0][2] == 'X') or (desk[1][0] == 'X' and desk[1][1] == 'X' and desk[1][2] == 'X') or (desk[2][0] == 'X' and desk[2][1] == 'X' and desk[2][2] == 'X'):
        return 'X'
    elif (desk[0][0] == 'X' and desk[1][0] == 'X' and desk[2][0] == 'X') or (desk[0][1] == 'X' and desk[1][1] == 'X' and desk[2][1] == 'X') or (desk[0][2] == 'X' and desk[1][2] == 'X' and desk[2][2] == 'X'):
        return 'X'
    elif (desk[0][0] == 'X' and desk[1][1] == 'X' and desk[2][2] == 'X') or (desk[0][2] == 'X' and desk[1][1] == 'X' and desk[2][0] == 'X'):
        return 'X'

    #Условия для ноликов
    if (desk[0][0] == 'O' and desk[0][1] == 'O' and desk[0][2] == 'O') or (desk[1][0] == 'O' and desk[1][1] == 'O' and desk[1][2] == 'O') or (desk[2][0] == 'O' and desk[2][1] == 'O' and desk[2][2] == 'O'):
        return 'O'
    elif (desk[0][0] == 'O' and desk[1][0] == 'O' and desk[2][0] == 'O') or (desk[0][1] == 'O' and desk[1][1] == 'O' and desk[2][1] == 'O') or (desk[0][2] == 'O' and desk[1][2] == 'O' and desk[2][2] == 'O'):
        return 'O'
    elif (desk[0][0] == 'O' and desk[1][1] == 'O' and desk[2][2] == 'O') or (desk[0][2] == 'O' and desk[1][1] == 'O' and desk[2][0] == 'X'):
        return 'O'

    return 'noOne'

# Функция которая будет выводить на экран игровую доску
def show_desk(d):
    n = 0
    print(" ",1,2,3)
    for strDesk in d:
        n = n + 1
        print(n,strDesk[0],strDesk[1],strDesk[2])

def init_desk():
    # Создадим пустую. "забьем" пустую матрицу пустыми значениями, чтоб отличать заполенные уже ячейки от пустых
    matrixList = []
    for i in range(3):
        yList = ["-","-","-"]
        matrixList.append(yList)
    return matrixList

if __name__ == '__main__':
    start_game()

