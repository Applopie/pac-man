#Главный исполняемый файл игры
#Здесь находятся функции, отвечающие за отрисовку кадров, вход и выход из игры
#Запустите его для начала игры
#

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
ellow = (227, 142, 14)



#Вызов других файлов игры
from WORLD import *
from PLAYER import *
from GHOSTS import *

pygame.init()

# Игравой экран
screen = pygame.display.set_mode([606, 666])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'RenderPlain.'


# Название экрана
pygame.display.set_caption('Pacman')

# Создание поверхности для рисования
background = pygame.Surface(screen.get_size())

# Черный фон
background.fill(black)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 20)

# Начальные положения для Пакмана и привидений
w = 303 - 16  # Width
p_h = (7 * 60) + 19  # Pacman height
m_h = (4 * 60) + 19  # Monster height
b_h = (3 * 60) + 19  # Binky height
i_w = 303 - 16 - 32  # Inky width
c_w = 303 + (32 - 16)  # Clyde width



##############
# СТАРТ ИГРЫ #
##############
def startGame():
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    cherry_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    flag = 0
    fg = 0
    bam = 0

    #Контроль за приведениями
    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0

    # Создание приведений и Пакмана как объектов
    Pacman = Player(w, p_h, "drawings/pacmanmain.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)

    Blinky = Ghost(w, b_h, "drawings/pacmancherry.png")
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky = Ghost(w, m_h, "drawings/pacmanpink.png")
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost(i_w, m_h, "drawings/pacmanblue.png")
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost(c_w, m_h, "drawings/pacmanorange.png")
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    # Отрисовка желтых шариков
    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(yellow, 4, 4)

                # Установка местоположения шариков
                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    # Добавление шариков в список объектов
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0
    level = 1

    done = False


    ##############################################
    ##### Игровой процесс, отрисовка кадров ######
    # (Исполняется, пока игрок не закончил игру) #
    ##############################################
    while done == False:
        current_time = pygame.time.get_ticks()
        ############################
        # Обработка нажатий клавиш #
        ############################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            old_x = Pacman.rect.left
            old_y = Pacman.rect.top
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pacman.rect.left -= 30
                    if not pygame.sprite.spritecollide(Pacman, wall_list, False):
                        Pacman.rect.left = old_x
                        Pacman.changespeed(-30, 0)
                        Pacman.image = Pacman.i[1][flag]
                        fg = 1
                    else:
                        Pacman.rect.left = old_x
                if event.key == pygame.K_RIGHT:
                    Pacman.rect.left += 30
                    if not pygame.sprite.spritecollide(Pacman, wall_list, False):
                        Pacman.rect.left = old_x
                        Pacman.changespeed(+30, 0)
                        Pacman.image = Pacman.i[0][flag]
                        fg = 0
                    else:
                        Pacman.rect.left = old_x
                if event.key == pygame.K_UP:
                    Pacman.rect.top -= 30
                    if not pygame.sprite.spritecollide(Pacman, wall_list, False):
                        Pacman.rect.top = old_y
                        Pacman.changespeed(0, -30)
                        Pacman.image = Pacman.i[2][flag]
                        fg = 2
                    else:
                        Pacman.rect.top = old_y
                if event.key == pygame.K_DOWN:
                    Pacman.rect.top += 30
                    if not pygame.sprite.spritecollide(Pacman, wall_list, False):
                        Pacman.rect.top = old_y
                        Pacman.changespeed(0, 30)
                        Pacman.image = Pacman.i[3][flag]
                        fg = 3
                    else:
                        Pacman.rect.top = old_y
        Pacman.image = Pacman.i[fg][flag]
        flag = (flag + 1) % 2

        ###############
        # ЛОГИКА ИГРЫ #
        ###############
        Pacman.update(wall_list, gate)

        returned = Pinky.changespeed(Pinky_directions, False, p_turn, p_steps, pl)
        p_turn = returned[0]
        p_steps = returned[1]
        Pinky.changespeed(Pinky_directions, False, p_turn, p_steps, pl)
        Pinky.update(wall_list, False)

        returned = Blinky.changespeed(Blinky_directions, False, b_turn, b_steps, bl)
        b_turn = returned[0]
        b_steps = returned[1]
        Blinky.changespeed(Blinky_directions, False, b_turn, b_steps, bl)
        Blinky.update(wall_list, False)

        returned = Inky.changespeed(Inky_directions, False, i_turn, i_steps, il)
        i_turn = returned[0]
        i_steps = returned[1]
        Inky.changespeed(Inky_directions, False, i_turn, i_steps, il)
        Inky.update(wall_list, False)

        returned = Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        c_turn = returned[0]
        c_steps = returned[1]
        Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        Clyde.update(wall_list, False)

        # Проверка на столкновение Пакмана с желтыми шариками
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)

        # Проверка списка столкновений
        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        if score == 3:
            cherry = Cherry(30 * 4 + 16, 30 * 10 + 16, 'drawings/cherry.png')
            cherry_list.add(cherry)
            all_sprites_list.add(cherry)

        if pygame.sprite.spritecollide(Pacman, cherry_list, True):
            deltime = current_time + 2000
            xb = Blinky.rect_x
            yb = Blinky.rect_y
            Blinky.kill()
            bam = 1

        if bam == 1:
            if current_time == deltime:
                Blinky = Ghost(303, 303, 'drawings/cherry.png')
                monsta_list.add(Blinky)
                all_sprites_list.add(Blinky)
                Blinky.update(wall_list, False)

        ##################
        # ОТРИСОВКА ИГРЫ #
        ##################
        screen.fill(black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, yellow)
        screen.blit(text, [10, 625])

        textadd1 = font.render("Уровень " + str(level), True, yellow)
        screen.blit(textadd1, [480, 625])

        if score == bll:
            doNext("Поздравляем! Вы выграли", 145, all_sprites_list, block_list, monsta_list, pacman_collide,
                   wall_list, gate)

        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

        if monsta_hit_list:
            doNext("Игра окончена", 235, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate)


        pygame.display.flip()

        clock.tick(10)



####################################
#### Отрисовка диалогового окна ####
####################################
def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    while True:

        # Выходим из игры или начинаем с начала?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        #Задняя часть диалогового окна
        w = pygame.Surface((400, 200))
        w.fill((250, 245, 115))
        screen.blit(w, (100, 200))

        # Выиграл или проиграл
        text1 = font.render(message, True, ellow)
        screen.blit(text1, [left, 233])

        text2 = font.render("Нажмите Enter, чтобы начать игру", True, ellow)
        screen.blit(text2, [130, 303])
        text3 = font.render("Нажмите Escape, чтобы покинуть игру", True, ellow)
        screen.blit(text3, [110, 333])

        pygame.display.flip()

        clock.tick(10)


startGame()

pygame.quit()
