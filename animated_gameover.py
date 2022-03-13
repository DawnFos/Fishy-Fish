import pygame, sys

SCREENRECT = pygame.Rect(0, 0, 812, 812)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('go1.png'))
        self.sprites.append(pygame.image.load('go2.png'))
        self.sprites.append(pygame.image.load('go3.png'))
        self.sprites.append(pygame.image.load('go4.png'))
        self.sprites.append(pygame.image.load('go5.png'))
        self.sprites.append(pygame.image.load('go6.png'))
        self.sprites.append(pygame.image.load('go7.png'))
        self.sprites.append(pygame.image.load('go8.png'))
        self.sprites.append(pygame.image.load('go9.png'))
        self.sprites.append(pygame.image.load('go10.png'))
        self.sprites.append(pygame.image.load('go11.png'))
        self.sprites.append(pygame.image.load('go12.png'))
        self.sprites.append(pygame.image.load('go1.png'))
        self.sprites.append(pygame.image.load('go2.png'))
        self.sprites.append(pygame.image.load('go3.png'))
        self.sprites.append(pygame.image.load('go4.png'))
        self.sprites.append(pygame.image.load('go5.png'))
        self.sprites.append(pygame.image.load('go6.png'))
        self.sprites.append(pygame.image.load('go7.png'))
        self.sprites.append(pygame.image.load('go8.png'))
        self.sprites.append(pygame.image.load('go9.png'))
        self.sprites.append(pygame.image.load('go10.png'))
        self.sprites.append(pygame.image.load('go11.png'))
        self.sprites.append(pygame.image.load('go12.png'))
        self.sprites.append(pygame.image.load('go1.png'))
        self.sprites.append(pygame.image.load('go2.png'))
        self.sprites.append(pygame.image.load('go3.png'))
        self.sprites.append(pygame.image.load('go4.png'))
        self.sprites.append(pygame.image.load('go5.png'))
        self.sprites.append(pygame.image.load('go6.png'))
        self.sprites.append(pygame.image.load('go7.png'))
        self.sprites.append(pygame.image.load('go8.png'))
        self.sprites.append(pygame.image.load('go9.png'))
        self.sprites.append(pygame.image.load('go10.png'))
        self.sprites.append(pygame.image.load('go11.png'))
        self.sprites.append(pygame.image.load('go12.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.sprites.append(pygame.image.load('goloser.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False ### will stop after one round

            self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 812
screen_height = 812
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game Over Animation")
pygame.mouse.set_visible(0)

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(0,0)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == pygame.KEYDOWN: ##### fish swims on keypress
        player.animate()

####################################Drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.20)
    pygame.display.flip()
    clock.tick(60)