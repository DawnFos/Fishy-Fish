
import pygame
from animatedmenu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 812, 812
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        pygame.display.set_caption('Fishy Fish')
        ############################################################check special font
        #self.font_special = pygame.freetype.SysFont(('jennifer.ttf'), 10)
        self.font_name = pygame.font.get_default_font()
        self.AQUA, self.WHITE = (51, 204, 204), (204, 51, 153)
        #self.fish = Player(0, 0)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu


    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.AQUA)
            
            self.draw_text('Thanks for Playing', 75, self.DISPLAY_W/2, self.DISPLAY_H/2)
            
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_animation(self):
        Trash() 
        Trash.images = [pygame.image.load(im) for im in ("can.png", "canalt.png")]
        trash = pygame.sprite.Group()
        Trash.containers = trash, all

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def background(self, x, y):
        bkgrnd = pygame.image.load('bluewater.gif').convert_alpha()
    #bkgrnd = pygame.image.load('bluewater.gif')
        background = pygame.Surface(SCREENRECT.size)
        for x in range(0, SCREENRECT.width, bkgrnd.get_width()):
            background.blit(bkgrnd, (x, 0))
        self.display.blit(background, (0,0))
        pygame.display.flip()
    #def special_text(self, text, size, x, y):
    #    font2 = pygame.font.Font(self.font_special, size)
    #    text_surface = font2.render(text, True, self.WHITE)
    #    text_rect = text_surface.get_rect()
    #    text_rect.center = (x,y)
    #    self.display.blit(text_surface,text_rect)



