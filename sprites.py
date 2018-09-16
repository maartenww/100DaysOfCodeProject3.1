import pygame as pg
import pygame as pg
from settings import *

vec = pg.math.Vector2
#TODO: ADD MOVING GROUND
class Spritesheet():

    def __init__(self,filename):
        self.spritesheet = pg.image.load_extended(filename)

    def get_img(self, x, y, width, height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image
#TODO: Add obstacles
class Ground(pg.sprite.Sprite):
    ground_sprite_width = 1600
    ground_sprite_height = 13
    ground_sprite_size = (ground_sprite_width, ground_sprite_height)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(((self.ground_sprite_size)))
        self.image = pg.image.load_extended('sprites/ground.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.ground_sprite_width,13 ))
        self.rect = self.image.get_rect()

        self.plat_pos_x = 0
        self.plat_pos_y = 750

        self.rect.x = self.plat_pos_x
        self.rect.y = self.plat_pos_y

        self.REAL_Y = self.rect.y - self.ground_sprite_height

class Player(pg.sprite.Sprite):

    player_sprite_width = 87 #73
    player_sprite_height = 94 #78

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = Spritesheet.get_img(Spritesheet('sprites/dino.png'), 0, 0, 87,94) #94
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (self.player_sprite_width, self.player_sprite_height))

        self.player_pos = vec(SCREEN_WIDTH / 8, 657)#SCREEN_HEIGHT / 1.375 -100

        self.rect.x = self.player_pos.x
        self.rect.y = self.player_pos.y


        self.player_vel = vec(0, 0)

        self.player_acc = vec(0, 0)

        self.canjump = False

    def jump(self):
        if self.canjump == True:

            self.player_vel.y = -10

    def pUpdate(self):
        self.player_acc = vec(0, PLAYER_GRAVITY)

        self.player_vel.y += self.player_acc.y

        self.player_pos.y += self.player_vel.y + 0.5 * self.player_acc.y

        self.rect.y = self.player_pos.y


        #print(str(self.player_vel.y))

    def handle(self, event):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_s]:
            print('duck')

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            print('space')
            self.jump()
            self.canjump = False

        elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
            self.player_acc.y = 0
