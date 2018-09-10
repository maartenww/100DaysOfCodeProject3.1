import pygame as pg
import sys
from settings import *

pg.init()



def main():
    while newGame1.isRunning:
        newGame1.create()
        newGame1.handle_events()
        newGame1.updateGame()

class newGame:
    isRunning = False

    def __init__(self):
        self.isRunning = True
        gameScreen = pg.display.set_mode((SCREEN_RESOLUTION))
        gameScreen.fill(GREY_WHITE)
        pg.display.set_caption('Die no gaem frumchrommmme')

    def create(self):
        pass

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.isRunning = False
                pg.quit()
                sys.exit()

    def updateGame(self):
        pg.display.update()

    def drawGame(self):
        pass
    

newGame1 = newGame()

if __name__ == "__main__":
    main()