from arcade import load_sound
import pygame
import random
from sys import exit
from pygame import mixer

"""is it possible to put this whole game in a function then call it from the MainMenu
    on the start game????? Also research how to loop back to MainMenu"""

pygame.init()
screen = pygame.display.set_mode ((812,812))
pygame.display.set_caption('Fishy Fishy')
clock = pygame.time.Clock()

SCORE = 0
MAX_RECYCLE = 5
TRASH_ODDS = 500
TRASH_RELOAD = 15
FALLTRASH_ODDS = 300
SCREENRECT = pygame.Rect(0, 0, 812, 812)

#############################            FISHY FISH              ######################
"""Note: Possible solution.Figure out how to intigrate the animated fish 
    into the __init__ function???"""
class Player(pygame.sprite.Sprite):
    speed = 10
    bounce = 20
    recy_offset = -10
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]#"""Can i insert the animation here?"""
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def shootcycle(self):
        pos = self.facing * self.recy_offset + self.rect.centerx
        return pos, self.rect.top

#############################            Keithan Truck          ################
"""Note: would like to make bigger and move across the screen at the same rate
    but desend much slower. Also size up the truck with possible only one truck 
    instead of multiples. Give the truck a life bar that is reduced on hits with
    the recycle. Possible laughing sound effect tided to the dropping of falling
    trash"""
class Trash(pygame.sprite.Sprite): 
    speed = 5
    animcycle = 4
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Trash.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 2]

#############################            Action after damage
class Morf(pygame.sprite.Sprite):
    #damage to fish

    defaultlife = 14
    animcycle = 5
    images = []

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life // self.animcycle % 2]
        if self.life <= 0:
            self.kill()

class Morftrash(pygame.sprite.Sprite):
    #damage to garbage ############ need an image for this maybe???????

    defaultlife = 10
    animcycle = 2
    images = []

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

##############################is this right??????
    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life // self.animcycle % 2]
        if self.life <= 0:
            self.kill()

#############################            Fish weapon
class Recycle(pygame.sprite.Sprite):
    """Can I make this rotate across the screen?"""
    speed = -8
    images = []

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos )

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()

#############################            Falling Garbage
class Fallingtrash(pygame.sprite.Sprite):
    speed = 4
    images = []

    def __init__(self, trash):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=trash.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 800:
            self.kill()

class Fallingcan(pygame.sprite.Sprite):
    speed = 5
    images = []

    def __init__(self, trash):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=trash.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 800:
            self.kill()

class Fallingbag(pygame.sprite.Sprite):
    speed = 2
    images = []

    def __init__(self, trash):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=trash.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 800:
            self.kill()

class Fallingcanalt(pygame.sprite.Sprite):
    speed = 6
    images = []

    def __init__(self, trash):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=trash.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 800:
            self.kill()

#############################            Score
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20) #####pick a font
        self.font.set_italic(1)
        self.color = "white"
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 800)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)

#############################            MAIN
def main(winstyle = 0):

    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        pygame.mixer = None

#############################            display

    winstyle = 0
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
#############################            images

    img = pygame.image.load('midfish.png')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]
    img = pygame.image.load('deadfish.png')
    Morf.images = [img, pygame.transform.flip(img, 0 , 0)]
    imgtm = pygame.image.load('flower.png')
    Morftrash.images = [imgtm, pygame.transform.flip(imgtm, 0, 0)]
    Trash.images = [pygame.image.load(im) for im in ("truck.png", "truck2.png")]
    Fallingtrash.images = [pygame.image.load('banana.png')]
    Fallingcan.images = [pygame.image.load('can.png')]
    Fallingcanalt.images = [pygame.image.load('canalt.png')]
    Fallingbag.images = [pygame.image.load('bag.png')]
    Recycle.images = [pygame.image.load('recycle.png')]

    #icon = pygame.transform.scale(Trash.images[0], (0, 0))
    #pygame.display.set_icon(icon)
    pygame.display.set_caption("Fishy Fish")
    pygame.mouse.set_visible(0)

#############################            background
    bkgrnd = pygame.image.load('bluewater.gif').convert_alpha()
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bkgrnd.get_width()):
        background.blit(bkgrnd, (x, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

#############################            sound effects
    shoot_sound = load_sound('bell.wav')
    boom_sound = load_sound('splash.wav')
    
####                 to do fix the soundtrack
    """if pygame.mixer:
        music = pygame.mixer.music.load('stream.wav')
        #pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)"""

####                 is this where the problem is?
#############################            game groups

    trash = pygame.sprite.Group()
    recycle = pygame.sprite.Group()
    fallingtrash = pygame.sprite.Group()
    fallingbag = pygame.sprite.Group()
    fallingcan = pygame.sprite.Group()
    fallingcanalt = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lasttrash = pygame.sprite.GroupSingle()

#############################            assign groups

    Player.containers = all
    Trash.containers = trash, all, lasttrash
    Recycle.containers = recycle, all
    Fallingtrash.containers = fallingtrash, all
    Fallingbag.containers = fallingbag, all
    Fallingcan.containers = fallingcan, all
    Fallingcanalt.containers = fallingcanalt, all
    Morf.containers = all
    Morftrash.containers = all
    Score.containers = all

    global score
    trashreload = TRASH_RELOAD
    score = 0
    clock = pygame.time.Clock()

    global SCORE
    player = Player()
    Trash()
    if pygame.font:
        all.add(Score())

#############################            Main loop                #####################
    while player.alive():
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()

        all.clear(screen, background)

        all.update()

#############################            input

        direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        player.move(direction)
        fire = keystate[pygame.K_SPACE]
        if not player.reloading and fire and len(recycle) < MAX_RECYCLE:
            Recycle(player.shootcycle())
            shoot_sound.play()
        player.reloading = fire

#############################            trash respawn

        if trashreload:
            trashreload = trashreload - 3
        elif not int(random.random() * TRASH_ODDS):
            Trash()
            trashreload = TRASH_RELOAD 

#############################            trashdrop

        if lasttrash and not int(random.random() * FALLTRASH_ODDS):
            Fallingbag(lasttrash.sprite)

        if lasttrash and not int(random.random() * FALLTRASH_ODDS):
            Fallingtrash(lasttrash.sprite)

        if lasttrash and not int(random.random() * FALLTRASH_ODDS):
            Fallingcan(lasttrash.sprite)

        if lasttrash and not int(random.random() * FALLTRASH_ODDS):
            Fallingcanalt(lasttrash.sprite)

#############################             recycle hits falling trash

        for fallingtrash in pygame.sprite.groupcollide(fallingtrash, recycle, 1, 1).keys():
            boom_sound.play()
            Morftrash(fallingtrash)
            SCORE = SCORE + 1
            return SCORE
            
        for fallingcan in pygame.sprite.groupcollide(fallingcan, recycle, 1, 1).keys():
            boom_sound.play()
            Morftrash(fallingcan)
            SCORE = SCORE + 1
            return SCORE
            
        for fallingcanalt in pygame.sprite.groupcollide(fallingcanalt, recycle, 1, 1).keys():
            boom_sound.play()
            Morftrash(fallingcanalt)
            SCORE = SCORE + 1
            return SCORE
            
        for fallingbag in pygame.sprite.groupcollide(fallingbag, recycle, 1, 1).keys():
            boom_sound.play()
            Morftrash(fallingbag)
            SCORE = SCORE + 1
            return SCORE
            
##############################           reycle hits truck

        for trash in pygame.sprite.groupcollide(trash, recycle, 1, 1).keys():
            boom_sound.play()
            Morftrash(trash)
            SCORE = SCORE + 1
            #return SCORE
            
#############################            trash hits fish ********make for all falling
#"""need to make option for all falling trash"""
        for fallingtrash in pygame.sprite.spritecollide(player, fallingtrash, 1):
            boom_sound.play()
            Morf(player)
            Morftrash(trash)
            #Morf(fallingtrash)
            player.kill()
        
#############################            truck and fish collide

        for trash in pygame.sprite.spritecollide(player, trash, 1):
            boom_sound.play()
            #Morftrash(trash)
            Morf(player)
            SCORE = SCORE - 1
            player.kill()
            

#############################            scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        clock.tick(60)
#############################            Print Game Over           ###########################
# print "Sad Panda 😔🐼, You are Green in the Gills"
#
#*************#Note#*************
#           Would like screan to display overlay of gameover image. for 10 or so seconds
#           then overlay playagain options, return to main menu or quit.
#
# class GameOver():
#    def __init__(self):
#        pygame.init()
#        self.running, self.playing = True, False
#        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
#        self.DISPLAY_W, self.DISPLAY_H = 812, 812
#        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
#        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
#        self.font_name = pygame.font.get_default_font()
#        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
#        self.play_again = PlayAgain(self)
#        self.main_menu = MainMenu(self)
#        self.quit = Quit(self)
#        self.curr_menu = self.main_menu
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#############################            Play Again?            ###############################

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(10000)

#############################            call game function

if __name__ == "__main__":
    main()
    pygame.quit()
