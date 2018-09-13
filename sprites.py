import pygame as pg
from settings import *


class Spritesheet():

    def __init__(self,filename):
        self.spritesheet = pg.image.load_extended(filename)

    def get_img(self, x, y, width, height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Ground(pg.sprite.Sprite):
    x_pos = 0
    y_pos = 900 / 1.30
    ground_pos = (x_pos, y_pos)
    ground_sprite_width = 1600
    ground_sprite_height = 19
    ground_sprite_size = (ground_sprite_width, ground_sprite_height)

    x_pos1 = ground_sprite_width
    y_pos1 = ground_sprite_height

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(((self.ground_sprite_size)))
        self.image = pg.image.load_extended('sprites/ground.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.ground_sprite_width,19 ))
        self.rect = self.image.get_rect()

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        all_sprites.add(self)

class Player(pg.sprite.Sprite):
    x_pos = 200
    y_pos = 900 / 1.375

    player_sprite_width = 73
    player_sprite_height = 78

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = Spritesheet.get_img(Spritesheet('sprites/dino.png'), 0, 0, 87,94)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (self.player_sprite_width, self.player_sprite_height))

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        all_sprites.add(self)

    def pUpdate(self): #Todo: Add player movement (Jumping and also add obastacles)
        pass
