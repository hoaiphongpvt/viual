import pygame, sys
from level import *
from menu import *

class Game(): 
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.screen_width, self.screen_height = 1200, 700
        self.display = pygame.Surface((self.screen_width,self.screen_height))
        self.window = pygame.display.set_mode(((self.screen_width,self.screen_height)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.quit = QuitMenu(self)
        self.curr_menu = self.main_menu
        self.level = Level(level_map[0],self.window,self,len(level_map) - 1)
        self.clock = pygame.time.Clock()
        self.title_music = pygame.mixer.Sound('audio/music.wav')
        self.bg_music = pygame.mixer.Sound('audio/bg.wav')

    def game_loop(self):
        if self.playing:
            self.bg_music.play(loops = -1)
            self.title_music.stop()
        while self.playing:
            self.check_events()
            self.window.blit(self.background, (0,0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)
            self.reset_keys()
        if self.playing == False:
            self.title_music.play(loops = -1)
            self.bg_music.stop()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                sys.exit()
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

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y) 
        self.display.blit(text_surface,text_rect)
    