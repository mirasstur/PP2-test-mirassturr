
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20

FPS = 15

COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),          # Обычная еда
    "dark_red": (139, 0, 0),     # Ядовитая еда
    "green": (0, 255, 0),        # Змея (по умолчанию)
    "blue": (0, 0, 255),         # Щит / интерфейс
    "yellow": (255, 255, 0),     # Бонус скорости
    "cyan": (0, 255, 255),       # Замедление
    "gray": (100, 100, 100),     # Препятствия
    "grid": (40, 40, 40)         # Сетка
}

DB_HOST = "localhost"
DB_NAME = "postegres" 
DB_USER = "postgres"
DB_PASS = "1234"