import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
ellow = (227, 142, 14)

class Wall(pygame.sprite.Sprite):
    # Конструктор
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        # Создание синих стен
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Локализация
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

#####################
# Создает все стены #
#####################
def setupRoomOne(all_sprites_list):
    # Делает стены
    wall_list = pygame.sprite.RenderPlain()

    # Список стен [x, y, width, height]
    walls = [[0, 0, 6, 600],
             [0, 0, 600, 6],
             [0, 600, 606, 6],
             [600, 0, 6, 606],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    # Проходим по списку. Создаем стену, добавляем ее в список
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # Возвращаем новый список
    return wall_list


def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, white))
    all_sprites_list.add(gate)
    return gate


# Класс создает желтые шарики, за которые дают очки
# Он является производным от класса "Sprite" в Pygame
class Block(pygame.sprite.Sprite):

    # Конструктор
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        # Создание шариков
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Локализация шариков
        self.rect = self.image.get_rect()

#Вишенки!!!
class Cherry(pygame.sprite.Sprite):

    # Конструктор
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("drawings/cherry.png").convert()

        # Локализация вишни
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

