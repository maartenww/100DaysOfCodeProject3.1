import pygame as pg
import sys
from settings import *
from sprites1 import *

pg.init()

gameScreen = pg.display.set_mode((SCREEN_RESOLUTION))
gameScreen.fill(WHITE)
pg.display.set_caption('Die no gaem frumchrommmme')

def main():
    while newGame1.isRunning:
        newGame1.handle_events()
        newGame1.updateGame()
        newGame1.drawGame()

class newGame:
    isRunning = False

    def __init__(self):
        self.isRunning = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.isRunning = False
                pg.quit()
                sys.exit()

    def updateGame(self):
        pg.display.update()
        all_sprites.update()
        #dinosaur.pUpdate()

    def drawGame(self):
        all_sprites.draw(gameScreen)

newGame1 = newGame()
ground1 = Ground()
dinosaur = Player()

if __name__ == "__main__":
    main()
