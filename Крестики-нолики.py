class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def greet():
    print(color.GREEN + "--------------------" + color.END)
    print(color.GREEN + " Приветствуем вас " + color.END)
    print(color.GREEN + "      В игре   " + color.END)
    print(color.GREEN + "  крестики-нолики  " + color.END)
    print(color.GREEN + "--------------------" + color.END)
    print(color.RED + " формат ввода: x y  " + color.END)
    print(color.PURPLE + " x - номер строки   " + color.END)
    print(color.PURPLE + " y - номер столбца  " + color.END)
    print(color.GREEN + "--------------------" + color.END)


greet()

field = [[" "] * 3 for i in range(3)]


def show():
    print()
    print(color.BOLD + "   | 0 | 1 | 2 | " + color.END)
    print(color.BOLD + " ---------------- " + color.END)
    for n, row in enumerate(field):
        row_str = f" {n} | {' | '.join(field[n])} | "
        print(color.BOLD + row_str + color.END)
        print(color.BOLD + " ---------------- " + color.END)
    print()


def ask():
    while True:
        cords = input(color.GREEN + "              Ваш ход: " + color.END).split()
        if len(cords) != 2:
            print(color.GREEN +" Введите 2 координаты! "+ color.END)
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(color.GREEN +" Введите числа! " + color.END)
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(color.GREEN +" Координаты вне диапазона! "+ color.END)
            continue

        if field[x][y] != " ":
            print(color.GREEN +" Клетка занята! "+ color.END)
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []

        for h in cord:
            symbols.append(field[h[0]][h[1]])

        if symbols == ["X", "X", "X"]:
            print(color.PURPLE + "Выиграл Х!!!" + color.END)
            return True
        if symbols == ["0", "0", "0"]:
            print(color.BLUE + "Выиграл 0!!!" + color.END)
            return True
    return False


turn = 0
while True:
    turn += 1

    show()

    if turn % 2 == 1:
        print(color.PURPLE + "Ходит крестик!" + color.END)
    else:
        print(color.BLUE + "Ходит нолик!" + color.END)

    x, y = ask()

    if turn % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        print(color.RED + "Поздравляем!!!")
        print("⠄⠄⠄⠄⠄⢀⣀⣠⡿⠒⢄⢠⣴⣶⠶⢦⣤⣤⠚⠛⠳⣄")
        print("⠄⠄⠄⠄⠘⣯⠉⠉⠄⠄⢀⣼⡿⢠⣶⡂⢀⣿⠆⠄⠄⠙⠛⢶⡆")
        print("⠄⠄⠄⣀⡤⠜⣧⠄⠄⠄⠙⠛⠿⣦⡏⠉⡿⡇⠄⠄⢀⡆⠄⣼⡇")
        print("⠄⠄⢠⠇⠐⢿⣟⠃⠄⠳⣾⠁⠄⠈⠙⣆⠁⣿⡶⠾⠋⣀⣴⡟⠁⢦⡄")
        print("⣾⠃⠄⠄⠄⠈⠻⣦⡀⠙⢷⡀⠄⠄⡼⢟⣩⡴⠶⠟⠛⠋⠁⠄⠸⡇")
        print("⣾⢱⠄⠄⢠⡆⠄⠈⣿⡀⠈⠻⡄⠜⣶⠋⠄⠄⠄⠄⣷⡀⠄⠄⠄⠙⢦⣄")
        print("⣼⡇⡞⠄⠄⣾⡇⠄⠰⠿⣧⣄⠄⠹⡄⠇⠄⠄⠄⠄⣰⣿⣧⡴⠃⢀⡔⢂⣿⣆")
        print("⣿⣷⣿⠄⠶⠿⣿⣤⠄⠄⠄⠙⢷⣄⠹⡀⠄⠄⢀⣴⠿⠛⠉⠄⣠⡏⣰⡏⠁")
        print("⢻⣇⣉⡥⠤⠤⢤⣍⡻⢦⡀⠄⠈⢿⡄⡇⠄⡴⠋⠁⣀⣤⣤⣚⣛⢁⡿")
        print("⠻⠋⠄⠄⠄⢷⣾⣽⣳⣝⢄⠄⠈⡇⠄⣨⢴⣚⣭⣽⡟⠄⠉⠉⠛⠁")
        print("⠄⠄⠄⠄⠄⠄⠄⠙⢿⣝⠛⠺⡂⠄⡣⡪⠒⠋⣉⣿⠟⠄⠄⠄⠄⠄⢀⠇")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠓⠄⠱⠜⢀⣀⡤⠖⠋⠁⠄⢀⣴⡠⠔⠚⠁⢰")
        print("⢠⡀⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⢠⣴⡶⠄⠄⠄⠄⠄⡔⠁⠄⣠⠔⠄⢠⡇")
        print("⡝⠦⣀⣄⣀⠄⠄⠄⠄⠄⠙⣦⢻⡅⠄⠄⠄⠄⠟⣸⡶⠟⠓⠄⠰⢛⠞")
        print("⠄⠘⣄⠈⡁⠄⠉⠑⡚⠗⠢⣄⡈⠢⠻⣿⠄⠄⣆⡾⠗⠄⣀⣤⠴⠚⠁")
        print("⠄⠄⢸⡦⠄⠁⢒⠶⠚⠒⢚⣳⣿⣶⡀⠙⣧⠄⠟⣀⠴⠒⠚⠓")
        print("⠄⠄⠄⠑⢦⣄⣁⠄⠄⠄⠁⠄⣀⠄⠄⢀⡈⠳⣄")
        print("⠄⠄⠄⠄⠄⠈⠩⠽⠯⠶⠞⠋⠁⠄⠄⠄⣹⣦⡙⣧⡀")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠛⢿⡌⣷⡀")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⡜⣇⡴")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣄⣀⣿⡇⣿⡇")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣇⡿⠁")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣽⣿⡟⠜")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⠿⠋" + color.END)
        break

    if turn == 9:
        print(color.YELLOW + "Ничья!" + color.END)
        break
