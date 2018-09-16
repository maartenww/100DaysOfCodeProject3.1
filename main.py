import pygame as pg
import sys
from settings import *
from sprites1 import *

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
        self.gameScreen = pg.display.set_mode((SCREEN_RESOLUTION))
        pg.display.set_caption('Die no gaem frumchrommmme')
        self.isRunning = True
        self.dinosaur = Player()
        self.ground = Ground()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.dinosaur,self.ground)
        self.players = pg.sprite.Group()
        self.players.add(self.dinosaur)
        self.grounds = pg.sprite.Group()
        self.grounds.add(self.ground)
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
        self.stry = self.myFont.render(str(int(self.dinosaur.player_pos.y)), False, (BLACK))
        self.ycolon = self.myFont.render('y: ',False,BLACK)
        self.dot = self.myFont.render('.',False,BLACK)
        pg.display.update()
        self.all_sprites.update()
        self.dinosaur.pUpdate()
        if pg.sprite.collide_rect(self.dinosaur, self.ground):
            self.dinosaur.player_pos.y = 657
            self.dinosaur.player_vel.y = 0
            self.dinosaur.canjump = True
    # Draw unto surface
    def drawGame(self):
        self.gameScreen.fill(WHITE)
        self.all_sprites.draw(self.gameScreen)
        self.gameScreen.blit(self.ycolon, (0,0))
        self.gameScreen.blit(self.stry, (25,0))
        self.gameScreen.blit(self.dot, (0, 657))
newGame1 = newGame()

if __name__ == "__main__":
    main()
