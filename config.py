from colorama import Back, Style

FIGURES = {
    1: [
        [[1, 1], [1, 1]],
    ],  # O
    2: [
        [[1], [1], [1], [1]],
        [[1, 1, 1, 1]],
    ],  # |
    3: [
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1], [1, 1], [1, 0]],
    ],  # Z
    4: [
        [[0, 1, 1], [1, 1, 0]],
        [[1, 0], [1, 1], [0, 1]],
    ],  # S
    5: [
        [[1, 1, 1], [0, 1, 0]],
        [[0, 1], [1, 1], [0, 1]],
        [[0, 1, 0], [1, 1, 1]],
        [[1, 0], [1, 1], [1, 0]],
    ],  # T
    6: [
        [[1, 0], [1, 0], [1, 1]],
        [[1, 1, 1], [1, 0, 0]],
        [[1, 1], [0, 1], [0, 1]],
        [[0, 0, 1], [1, 1, 1]],
    ],  # L
    7: [
        [[0, 1], [0, 1], [1, 1]],
        [[1, 0, 0], [1, 1, 1]],
        [[1, 1], [1, 0], [1, 0]],
        [[1, 1, 1], [0, 0, 1]],
    ],  # J
}

# Скорость падения фигуры
START_TIME_DECLINE_FIGURE = 1

# Вес, для определения кол-ва очков для перехода на уровень
WEIGHT_LEVELS = 5
COUNT_LEVELS = 10

# Начальная позиция счетчика очков и размер его инкрементации
START_SCORE_VALUE = 0
SCORE_INCREMENT = 100

# Размер игрового поля
WEIGHT_GRID = 10
HEIGHT_GRID = 20

# Спрятанные линии сверху, от куда будет падать фигура
COUNT_HIDDEN_LINES = 2

# Цвета состояния фигур
ACTIVE_FIGURE = "".join([Back.BLUE,  '  ', Style.RESET_ALL])
FIGURE_ON_MATRIX = "".join([Back.GREEN, '  ', Style.RESET_ALL])
BACKGROUND_MATRIX = "".join([Back.RED,   '  ', Style.RESET_ALL])
