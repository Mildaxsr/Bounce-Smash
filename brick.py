from config import *


class Brick:
    def __init__(self, x, y, color='green', strength=1):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.strength = strength
        self.base_color = color
        self.update_color()

    def update_color(self):
        """Обновление цвета кирпича в зависимости от прочности"""
        if self.strength == 2:
            self.color = (255, 165, 0)
        elif self.strength == 1:
            self.color = self.base_color
        else:
            self.color = BLACK

    def draw(self):
        """Отрисовка кирпича"""
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def hit(self):
        """Обработка удара по кирпичу"""
        self.strength -= 1
        self.update_color()
        return self.strength <= 0  # Удалить, если прочность 0



# Функции для создания уровней с различными кирпичами

def create_bricks_level_1():
    """Создание кирпичей для уровня 1 (стандартные синие кирпичи)"""
    bricks = []
    for i in range(1, BRICK_ROWS):
        for j in range(BRICK_COLS):
            x = j * (BRICK_WIDTH + 5) + 20
            y = i * (BRICK_HEIGHT + 5) + 20
            bricks.append(Brick(x, y, color='blue'))
    return bricks

def create_bricks_level_2():
    """Создание кирпичей для уровня 2 (чередующиеся красные и зеленые кирпичи)"""
    bricks = []
    for i in range(1, BRICK_ROWS):
        for j in range(BRICK_COLS):
            x = j * (BRICK_WIDTH + 5) + 20
            y = i * (BRICK_HEIGHT + 5) + 20
            color = RED if (i + j) % 2 == 0 else GREEN
            bricks.append(Brick(x, y, color=color))
    return bricks

def create_bricks_level_3():
    """Создание кирпичей для уровня 3 (укрепленные кирпичи с разной прочностью)"""
    bricks = []
    for i in range(1, BRICK_ROWS):
        for j in range(BRICK_COLS):
            x = j * (BRICK_WIDTH + 5) + 20
            y = i * (BRICK_HEIGHT + 5) + 20
            strength = 2 if (i + j) % 2 == 0 else 1
            bricks.append(Brick(x, y, color='yellow', strength=strength))
    return bricks
