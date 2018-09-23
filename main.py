import pygame as pg
import sys
from settings import *
from sprites1 import *
import time

pg.init()


def main():
    # Gameloop
    while newGame1.isRunning:
        newGame1.handle_events()
        newGame1.updateGame()
        newGame1.drawGame()

# Game Class
class newGame:
    isRunning = False

    # Constructor
    def __init__(self):

        # Init game window
        self.gameScreen = pg.display.set_mode((SCREEN_RESOLUTION))
        pg.display.set_caption('Die no gaem frumchrommmme')

        # Gamestate boolean
        self.isRunning = True

        # ---------------------
        # Instantiate everything

        # Ground and player instantiate
        self.dinosaur = Player()
        self.ground01 = Ground()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.dinosaur,self.ground01)
        self.players = pg.sprite.Group()
        self.players.add(self.dinosaur)
        self.grounds = pg.sprite.Group()
        self.grounds.add(self.ground01)

        # Instantiate cacti
        self.bigCacti01 = BigCactus01()
        self.smallCacti01 = SmallCactus01()
        self.bigCacti = pg.sprite.Group()
        self.smallCacti = pg.sprite.Group()
        self.Cacti = pg.sprite.Group()
        self.bigCacti.add(self.bigCacti01)
        self.smallCacti.add(self.smallCacti01)
        self.Cacti.add(self.bigCacti01)
        self.Cacti.add(self.smallCacti01)
        self.all_sprites.add(self.bigCacti01)
        self.all_sprites.add(self.smallCacti01)

        for x in range(10): #TODO Add procedural generation with cacti
            cacti.append(BigCactus01())
        for z in cacti:
            self.bigCacti.add(z)
            self.Cacti.add(z)
            self.all_sprites.add(z)
        # ---------------------

        # Load font
        self.myFont = pg.font.SysFont('Arial Black MS', 30)

    # Handle events
    def handle_events(self):
        for event in pg.event.get():
            # Movement controls handle
            Player.handle(self.dinosaur, event)
            # Quits if 'x' is clicked
            if event.type == pg.QUIT:
                self.isRunning = False
                pg.quit()
                sys.exit()

    # Poll and update game
    def updateGame(self):

        # Update y-position information
        self.stry = self.myFont.render(str(int(self.dinosaur.player_pos.y)), False, (BLACK))
        self.ycolon = self.myFont.render('y: ',False,BLACK)
        self.dot = self.myFont.render('.',False,BLACK)

        pg.display.update()
        self.all_sprites.update()
        self.dinosaur.pUpdate()
        if pg.sprite.collide_rect(self.dinosaur, self.ground01):
            self.dinosaur.player_pos.y = 657
            self.dinosaur.player_vel.y = 0
            self.dinosaur.canjump = True
        self.smallCacti01.cacUpdate()
        self.bigCacti01.cacUpdate()
        self.ground01.update_ground()

        for y in cacti: #TODO: ADD PROCEDURAL GENERATION
            y.cacUpdate()

    # Draw unto surface
    def drawGame(self):
        # Paint background white
        self.gameScreen.fill(WHITE)

        # Draw all sprites
        self.all_sprites.draw(self.gameScreen)

        # Draw y position live on screen
        self.gameScreen.blit(self.ycolon, (0,0))
        self.gameScreen.blit(self.stry, (25,0))
        self.gameScreen.blit(self.dot, (0, 657))

# Instnatiate new game class
newGame1 = newGame()

if __name__ == "__main__":
    main()
