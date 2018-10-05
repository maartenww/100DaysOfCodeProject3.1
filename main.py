import pygame as pg
import sys
from settings import *
from sprites1 import *
import time
import random

pg.init()


def main():
    # Gameloop
    while newGame1.isRunning:
        newGame1.handle_events()
        newGame1.updateGame()
        newGame1.drawGame()
        if newGame1.gameOver == True:
            newGame1.gameOverScreen()
        elif newGame1.gameOver == False:
            continue


# Game Class
class newGame:
    isRunning = False
    gameOver = False

    # Constructor
    def __init__(self):

        # Init game window
        self.gameScreen = pg.display.set_mode((SCREEN_RESOLUTION))
        pg.display.set_caption('Die no gaem frumchrommmme')

        # Clock init
        self.clock = pg.time.Clock()

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

        # <---------------------------------------------------------->

        # Instantiate cacti (Kinda for testing) (Again individual sprites)
        #self.bigCacti01 = BigCactus01()
        #self.smallCacti01 = SmallCactus01()

        # <---------------------------------------------------------->


        # Cactus sprite group init
        self.bigCacti = pg.sprite.Group()
        self.smallCacti = pg.sprite.Group()
        self.Cacti = pg.sprite.Group()

        # Instantiate cacti Part2
        for x in range(4): # 4 Meaning the number of cacti
            cacti.append(SmallCactus01()) # We're adding 4 small cacti to the cacti list
            #cacti.append(BigCactus01()) # We're adding 4 big cacti to the cacti list
            for cactus in cacti: # For each cactus in the cacti list we do the following:
                cactus.add(self.Cacti) # We add the cactus object to the Cacti SPRITE GROUP
                cactus.add(self.all_sprites) # We add the cactus object to the ALL SPRITES SPRITES GROUP
                #print(cactus.cactus_pos.x, cactus.cactus_pos.y) # We print the position of the cactus (testing)
                cactus.cactus_pos.x += (random.randint(800,2400)) # We make sure each cactus has a different position and is far away from each other between 800 and 2400


        # <------------------------------------>

        # Adding individual sprites to group (kinda for testing)
        #self.bigCacti.add(self.bigCacti01)
        #self.smallCacti.add(self.smallCacti01)
        #self.Cacti.add(self.bigCacti01, self.smallCacti01)
        #self.all_sprites.add(self.bigCacti01, self.smallCacti01)

        # <------------------------------------>

        self.button01 = replayButton()
        self.buttons = pg.sprite.Group()
        self.buttons.add(self.button01)

        self.GOF01 = gameOverFont()
        self.GOFS = pg.sprite.Group()
        self.GOFS.add(self.GOF01)

        # Load font
        self.myFont = pg.font.SysFont('Arial Black MS', 30)

    # Handle events
    def handle_events(self):
        for event in pg.event.get():
            # Movement controls handle
            Player.handle(self.dinosaur, event)
            replayButton.handleButton(self.button01, event, self.gameOver)
            isClicked = replayButton.handleButton(self.button01, event, self.gameOver)
            if isClicked == 1:
                self.restartGame()
            # Quits if 'x' is clicked
            if event.type == pg.QUIT:
                self.isRunning = False
                pg.quit()
                sys.exit()

        # For checking mouse pos (debugging)
        #print(str(mouse[0]), str(mouse[1]))

    # Poll and update game
    def updateGame(self):

        #self.score = (int((pg.time.get_ticks()) / 100))

        self.clock.tick(FPS)

        hits = pg.sprite.spritecollide(self.dinosaur, self.Cacti, False, pg.sprite.collide_mask)

        # Update y-position information
        self.stry = self.myFont.render(str(int(self.dinosaur.player_pos.y)), False, (BLACK))
        self.ycolon = self.myFont.render('y: ',False,BLACK)
        self.dot = self.myFont.render('.',False,BLACK)

        # Update score info
        #self.score = self.myFont.render(str(int((pg.time.get_ticks()) / 100)), False, (BLACK))
        self.scoreText = self.myFont.render('Score: ', False, BLACK)

        # New Score


        # Update screen
        pg.display.update()

        # Update sprites
        self.all_sprites.update()

        # Update information
        self.dinosaur.pUpdate()

        # Sprite collision
        if pg.sprite.collide_rect(self.dinosaur, self.ground01):
            self.dinosaur.player_pos.y = 657
            self.dinosaur.player_vel.y = 0
            self.dinosaur.canjump = True

        if hits:
            self.gameOver = True

        #if pg.sprite.collide_rect_ratio(0.7):


        # <------------------------------------------------------------------->

        # Update additional information (Only for testing, individual cactus updating)
        #self.smallCacti01.cacUpdate()
        #self.bigCacti01.cacUpdate()

        # <------------------------------------------------------------------->


        # Update the ground with the unique update_ground method in the ground01 class
        self.ground01.update_ground()


        # For each cactus in the cacti list we use the unique cacUpdate method as well as print the position
        for cactus in cacti:
            cactus.cacUpdate()
            self.score = self.myFont.render(str(int(cactus.cacScore)), False, BLACK)

    # Draw unto surface
    def drawGame(self):
        # Paint background white
        self.gameScreen.fill(WHITE)

        # Draw all sprites
        self.all_sprites.draw(self.gameScreen)

        # Draw y position live on screen
        #self.gameScreen.blit(self.ycolon, (0,0))
        #self.gameScreen.blit(self.stry, (25,0))

        # Draw score
        self.gameScreen.blit(self.scoreText, (35, 10))
        self.gameScreen.blit(self.score, (100, 10))

        # Draw game over
        #   Nothing yet

    # Restart game method
    def restartGame(self):
        for cactus in cacti:
            cactus.cacScore = 0
            cactus.Cactus_speed = 0
        self.isRunning = False
        # Reset score
    def gameOverScreen(self):
        self.buttons.draw(self.gameScreen)
        self.GOFS.draw(self.gameScreen)

# Instnatiate new game class
newGame1 = newGame()

if __name__ == "__main__":
    main()
