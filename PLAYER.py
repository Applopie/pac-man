import pygame

class Player(pygame.sprite.Sprite):
    # Set speed vector
    change_x = 0
    change_y = 0

    # Constructor function
    def __init__(self, x, y, filename):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.i = ((pygame.image.load("drawings/pacmanmainr.png").convert(), pygame.image.load("drawings/pacmanmainrc.png").convert()),
             (pygame.image.load("drawings/pacmanmainl.png").convert(), pygame.image.load("drawings/pacmanmainlc.png").convert()),
             (pygame.image.load("drawings/pacmanmainu.png").convert(), pygame.image.load("drawings/pacmanmainuc.png").convert()),
             (pygame.image.load("drawings/pacmanmaind.png").convert(), pygame.image.load("drawings/pacmanmaindc.png").convert()))
        #self.i_r = (pygame.image.load("drawings/pacmanmainr.png").convert(), pygame.image.load("drawings/pacmanmainrc.png").convert())
        #self.i_l = (pygame.image.load("drawings/pacmanmainl.png").convert(), pygame.image.load("drawings/pacmanmainlc.png").convert())
        #self.i_u = (pygame.image.load("drawings/pacmanmainu.png").convert(), pygame.image.load("drawings/pacmanmainuc.png").convert())
        #self.i_d = (pygame.image.load("drawings/pacmanmaind.png").convert(), pygame.image.load("drawings/pacmanmaindc.png").convert())

        self.image = pygame.image.load(filename).convert()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y
        self.time = None


    # Change the speed of the player
    def changespeed(self, vx, vy):
        self.change_x = vx
        self.change_y = vy

    # Find a new position for the player
    def update(self, walls, gate):
        # Get the old position, in case we need to go back to it

        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y

        # Did this update cause us to hit a wall?
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            # Whoops, hit a wall. Go back to the old position
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


# Inheritime Player klassist