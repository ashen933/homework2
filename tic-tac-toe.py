import pygame
import sys
import random


def blit_text(surface, text, pos, font,
              color=pygame.Color('white')):  # отображает текст
    words = [word.split(' ') for word in text.splitlines()
             ]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def start_screen():
    screen.fill((0, 0, 0))
    t = 'Игра : крестики-нолики 10Х10 . \nПравила просты,  проигрывает тот, у кого получился вертикальный, горизонтальный или диагональный ряд из пяти своих фигур. \nДля начала игры нажмите Enter. \nДля старта новой игры нажмите Пробел. \nУдачной игры '
    font = pygame.font.SysFont('Arial', 30)
    blit_text(screen, t, (20, 20), font)


def new_game():  # перезапускает игру
    global array_values
    global game_over
    global first_gamer
    array_values = [[0] * amount_cell
                    for i in range(amount_cell)]  # значения в ячейке
    game_over = False
    first_gamer = random.choice(('computer', 'gamer'))
    screen.fill((0, 0, 0))


def board_game():  # отрисовывает поле ячеек для игры
    for i in range(amount_cell):
        for j in range(amount_cell):
            x = size_block * i + size_border * (i + 1)
            y = size_block * j + size_border * (j + 1)
            if array_values[j][i] == 'X':
                color = (255, 100, 100)

            elif array_values[j][i] == 'O':
                color = (100, 100, 255)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == (255, 100, 100):
                pygame.draw.line(screen, (0, 0, 0), (x, y),
                                 (x + size_block, y + size_block), 4)
                pygame.draw.line(screen, (0, 0, 0), (x + size_block, y),
                                 (x, y + size_block), 4)
            elif color == (100, 100, 255):
                pygame.draw.circle(screen, (0, 0, 0),
                                   (x + size_block / 2, y + size_block / 2),
                                   size_block / 2, 4)


def array_diagonals(matrix):  # получает матрицу и возвращает список диагоналей
    L = len(matrix)
    diagonals1 = [[] for i in range(L + L - 1)]
    for i in range(-(L - 1), L):
        for j in range(L):
            row, col = j, i + j
            if 0 <= row < L and 0 <= col < len(matrix[0]):
                diagonals1[i + L - 1].append(matrix[row][col])

    diagonals2 = [[] for i in range(L + L - 1)]
    for i in range(-(L - 1), L):
        for j in range(L):
            row, col = j, i + j
            if 0 <= row < L and 0 <= col < len(matrix[0]):
                diagonals2[i + len(matrix) - 1].append(matrix[row][L - col -
                                                                   1])
    list_diagonals = []
    for i in diagonals1:
        if len(i) > 4:
            list_diagonals.append(i)
    for i in diagonals2:
        if len(i) > 4:
            list_diagonals.append(i)
    return list_diagonals


def check_win(array, sign):  # проверяет условие победы-проигрыша для 'X' и '0'
    zeroes = 0
    transp_array = [[array[j][i] for j in range(len(array))]
                    for i in range(len(array))]

    for i in array:

        zeroes += i.count(0)

        if str(sign * 5) in ''.join([str(j) for j in i]):
            print('Победа')
            return sign
    for i in transp_array:

        if str(sign * 5) in ''.join([str(j) for j in i]):
            print('Победа')
            return sign
    for i in array_diagonals(array):
        if str(sign * 5) in ''.join([str(j) for j in i]):
            print('Победа')
            return sign

    if zeroes == 0:
        return 'Ничья'
    return False


def input_data():  # получает вводимые игроком данные
    global trigger
    if trigger == 1:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            column = x_pos // (size_border + size_block)
            row = y_pos // (size_border + size_block)
            if array_values[row][column] == 0:
                if first_gamer == 'gamer':
                    array_values[row][column] = 'X'
                elif first_gamer == 'computer':
                    array_values[row][column] = 'O'

                trigger = 0


def ai_computer():  # поведение компьютера
    global trigger
    if trigger == 0:
        j = random.randint(0, amount_cell - 1)
        i = random.randint(0, amount_cell - 1)
        if array_values[j][i] == 0:
            if first_gamer == 'gamer':
                array_values[j][i] = 'O'
            elif first_gamer == 'computer':
                array_values[j][i] = 'X'
            trigger = 1


amount_cell = 10  # количество ячеек в границе квадрата
size_block = 50  # размер ячейки под символы
size_border = 5  # размер границы между ячейками
width_screen = height_screen = amount_cell * size_block + (
    amount_cell + 1
) * size_border  # ширина и высота окна как количество ячеек в игре + растояние между ячейками
array_values = [[0] * amount_cell
                for i in range(amount_cell)]  # значения в ячейке
first_gamer = random.choice(
    ('computer',
     'gamer'))  # Определяет за кем первый ход. Первый ходит "Х", второй "O".
if first_gamer == 'computer':
    trigger = 1  # триггер переключения хода с игроками на компьютер. При единице ходит игрок
elif first_gamer == 'gamer':
    trigger = 0

start_game = 0
pygame.init()

screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption(
    'Обратные крестики нолики - пять в ряд')  # заголовок окна

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            new_game()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and start_game == 0:
            start_game = 1
            screen.fill((0, 0, 0))

    if start_game == 0:
        start_screen()

    if not game_over and start_game == 1:
        board_game()
        input_data()
        ai_computer()
        if check_win(array_values, 'O') == 'Ничья':
            game_over = 'Ничья'
        elif check_win(array_values, "O"):
            game_over = 'Проиграл ' + 'O'
        elif check_win(array_values, "X"):
            game_over = 'Проиграл ' + 'X'

    elif game_over:
        screen.fill((0, 0, 0))
        text = pygame.font.SysFont('arial',
                                   100).render(game_over, True,
                                               (255, 255, 255))
        x_cord = screen.get_width() / 2 - text.get_rect().width / 2
        y_cord = screen.get_height() / 2 - text.get_rect().height / 2
        screen.blit(text, (x_cord, y_cord))

    pygame.display.flip()  # отрисовка экрана
