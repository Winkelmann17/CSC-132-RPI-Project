# pygame iteration
import pygame as pg
import pygame_gui as gui

from time import sleep

import sys


class Game:

    def __init__(self):
        pass

    def setupGUI(self):
        global screen
        pg.display.set_caption("Dance Dance Pi-Volution")
        screen = pg.display.set_mode((WIDTH, HEIGHT))

        global background
        background = pg.image.load("ddr background.jpg")
        
        global manager
        manager = gui.UIManager((WIDTH, HEIGHT))
        print("manager check")
        
        #start_button = gui.elements.UIButton(relative_rect=pg.Rect((350,275), (100, 50)),text= 'Press to Begin', manager=manager)
        print("button check")
        
        global clock
        clock = pg.time.Clock()
        global running
        running = True
        print("GUI check")

    def setupArrows(self):
        global all_sprites
        all_sprites = pg.sprite.Group()

        global DOWN_GRAY
        DOWN_GRAY = stillArrow(WIDTH / 2 + 80, 70, "ddr outline down.png")
        all_sprites.add(DOWN_GRAY)

        global UP_GRAY
        UP_GRAY = stillArrow(WIDTH / 2 - 80, 70, "ddr outline up.png")
        all_sprites.add(UP_GRAY)

        global RIGHT_GRAY
        RIGHT_GRAY = stillArrow(WIDTH / 2 + 230, 70, "ddr outline right.png")
        all_sprites.add(RIGHT_GRAY)
        
        global LEFT_GRAY
        LEFT_GRAY = stillArrow(WIDTH / 2 - 230, 70, "ddr outline left.png")
        all_sprites.add(LEFT_GRAY)

        global DOWN_MOVER
        DOWN_MOVER = Arrow(WIDTH/2 + 80, 1000, "ddr arrows.png")
        all_sprites.add(DOWN_MOVER)

        global UP_MOVER
        UP_MOVER = Arrow(WIDTH/2 - 80, 1000, "ddr arrows up.png")
        all_sprites.add(UP_MOVER)

        global RIGHT_MOVER
        RIGHT_MOVER = Arrow(WIDTH/2 + 230, 1000, "ddr arrows right.png")
        all_sprites.add(RIGHT_MOVER)

        global LEFT_MOVER
        LEFT_MOVER = Arrow(WIDTH/2 - 230, 1000, "ddr arrows left.png")
        all_sprites.add(LEFT_MOVER)

    def setupScore(self):
        pg.font.init()

        global font
        font = pg.font.Font('freesansbold.ttf', 32)
        print("font check")
        
        global textX
        global textY
        textX = 10
        textY = 10

##        score = font.render("Score : {}".format(str(score_value)), True, (0, 0, 0,))
##
##        screen.blit(score, (
class stillArrow(pg.sprite.Sprite):

    def __init__(self, x, y, img_path):
        super().__init__()

        self.x = x
        self.y = y

        self.image = pg.image.load(img_path).convert_alpha()

        self.size = self.image.get_size()
        self.image = pg.transform.scale(self.image, (int(self.size[0] *(0.27)), int(self.size[1] * (0.27))))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)

##        self.size = self.image.get_size()
##        self.image = pg.transform.scale(self.image, (int(self.size[0] *(1/4)), int(self.size[1] * (1/4))))



class Arrow(pg.sprite.Sprite):

    def __init__(self, x, y, img_path):
        super().__init__()

        self.image = pg.image.load(img_path).convert_alpha()

        self.size = self.image.get_size()
        self.image = pg.transform.scale(self.image, (int(self.size[0] *(1/4)), int(self.size[1] * (1/4))))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)

        self.dx = 0
        self.dy = -2
        self.position = y


    def arrowMove(self):
        pass

    def update(self):
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        self.position -= 2
        

def ShowScore(score_value):
    global score
    score = font.render("Score : {}".format(str(score_value)), True, (0, 0, 0,))
    
# ------------------ Main Program -----------------------------------------------------#
WIDTH = 1200
HEIGHT = 800

g = Game()
print("class check")

g.setupGUI()

global all_sprites


g.setupArrows()

score_value = 0
g.setupScore()

while running:
    time_delta = clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            #sys.exit

        if event.type == pg.USEREVENT:
            if event.user_type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    print("Welcome to DDR!")
                    
        if event.type == pg.KEYDOWN :
            if event.key == pg.K_DOWN and (DOWN_MOVER.position > (DOWN_GRAY.rect.y + 56) - 10) and (DOWN_MOVER.position < (DOWN_GRAY.rect.y + 56) + 10):
                score_value += 1
                print(score)
                
            if event.key == pg.K_UP and (UP_MOVER.position > (UP_GRAY.rect.y + 56) - 10) and (UP_MOVER.position < (UP_GRAY.rect.y + 56) + 10):
                score_value += 1
                print(score)

            if event.key == pg.K_RIGHT and (RIGHT_MOVER.position > (RIGHT_GRAY.rect.y + 56) - 10) and (RIGHT_MOVER.position < (RIGHT_GRAY.rect.y + 56) + 10):
                score_value += 1
                print(score)

            if event.key == pg.K_LEFT and (LEFT_MOVER.position > (LEFT_GRAY.rect.y + 56) - 10) and (LEFT_MOVER.position < (LEFT_GRAY.rect.y + 56) + 10):
                score_value += 1
                print(score)
        manager.process_events(event)

        
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()

    ShowScore(score_value)
    
    
    #manager.update(time_delta)
    screen.blit(background, (0,0))
    screen.blit(score, (textX, textY))
    #manager.draw_ui(screen)
    #pg.display.update()
