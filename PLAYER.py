import pygame

class Player(pygame.sprite.Sprite):
    # Вектор скорости
    change_x = 0
    change_y = 0

    # Конструктор
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        # Изображения для анимации пакмана
        self.i = ((pygame.image.load("drawings/pacmanmainr.png").convert(), pygame.image.load("drawings/pacmanmainrc.png").convert()),
             (pygame.image.load("drawings/pacmanmainl.png").convert(), pygame.image.load("drawings/pacmanmainlc.png").convert()),
             (pygame.image.load("drawings/pacmanmainu.png").convert(), pygame.image.load("drawings/pacmanmainuc.png").convert()),
             (pygame.image.load("drawings/pacmanmaind.png").convert(), pygame.image.load("drawings/pacmanmaindc.png").convert()))

        self.image = pygame.image.load(filename).convert()

        # Локализация Пакмана
        self.rect = self.image.get_rect()
        self.rect_x = x
        self.rect_y = y
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y
        self.time = None


    # Изменение скорости Пакмана
    def changespeed(self, vx, vy):
        self.change_x = vx
        self.change_y = vy

    # Нахождение новой позиции игрока
    def update(self, walls, gate):
        # Сохранение старой позиции на случай, если нам потребуется вернуться обратно

        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y

        # Перемещение приводит к проламыванию стены?
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            # Возвращайся на старую позицию
            self.rect.left = old_x
        else:

            self.rect.top = new_y

            # Did this update cause us to hit a wall?
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                # Whoops, hit a wall. Go back to the old position
                self.rect.top = old_y

        if gate != False:
            gate_hit = pygame.sprite.spritecollide(self, gate, False)
            if gate_hit:
                self.rect.left = old_x
                self.rect.top = old_y


