import pygame as pg
from settings import *

vec = pg.math.Vector2

#TODO: ADD Multiple obstacle generation

class Spritesheet():

    def __init__(self,filename):
        self.spritesheet = pg.image.load_extended(filename)

    def get_img(self, x, y, width, height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Ground(pg.sprite.Sprite):
    ground_sprite_width = 3200
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

    def update_ground(self):
        self.rect.x -= 5
        if self.rect.x <= -1600:
            self.rect.x = 0

class Player(pg.sprite.Sprite):

    player_sprite_width = 87 #73
    player_sprite_height = 94 #78

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.load_images()
        #self.image = Spritesheet.get_img(Spritesheet('sprites/dino.png'), 0, 0, 87,94) #94
        self.image = self.walking_images[0]
        self.rect = self.image.get_rect()
        #self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (self.player_sprite_width, self.player_sprite_height))

        self.player_pos = vec(SCREEN_WIDTH / 8, 657)#SCREEN_HEIGHT / 1.375 -100

        self.rect.x = self.player_pos.x
        self.rect.y = self.player_pos.y


        self.player_vel = vec(0, 0)

        self.player_acc = vec(0, 0)

        self.canjump = False

        self.current_frame = 0
        self.last_update = 0
        self.walking = True

    def jump(self):
        if self.canjump == True:

            self.player_vel.y = -10

    def pUpdate(self):
        self.player_acc = vec(0, PLAYER_GRAVITY)

        self.player_vel.y += self.player_acc.y

        self.player_pos.y += self.player_vel.y + 0.5 * self.player_acc.y

        self.rect.y = self.player_pos.y

        self.animate()

    def load_images(self):
        self.walking_images = [Spritesheet.get_img(Spritesheet('sprites/dino.png'), 176, 0, 87, 94),

                       Spritesheet.get_img(Spritesheet('sprites/dino.png'), 264, 0, 87, 94)]
        self.standing_image = [Spritesheet.get_img(Spritesheet('sprites/dino.png'),0, 0, 87, 94)]
        for image in self.walking_images:
            image.set_colorkey(BLACK)

    def animate(self):
        now = pg.time.get_ticks()
        if self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_images)

        self.image = self.walking_images[self.current_frame]
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

class Cactus(pg.sprite.Sprite):

    Cactus_sprite_width = 50
    Cactus_sprite_length = 100
    Cactus_speed = 5

    framenumber = 0

    def __init__(self, cactus_pos, cactus_speed):

        pg.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image,(self.Cactus_sprite_width,self.Cactus_sprite_length))

        self.cactus_pos = cactus_pos
        self.cactus_pos = vec(SCREEN_WIDTH, 657)

        self.rect.x = self.cactus_pos.x
        self.rect.y = self.cactus_pos.y

        self.Cactus_speed = cactus_speed

        for i in range(len(cacti)):
            cacti[i].cactus_pos.x = int(i * 2) #TODO: Make procedural cactus generation

    def cacUpdate(self):
        self.cactus_pos.x -= self.Cactus_speed

        self.rect.x = self.cactus_pos.x
        self.rect.y = self.cactus_pos.y

        if self.cactus_pos.x < 0: #TODO: 'ADD self.cactus_pos.x = 1599' if you want cacti spawning each time...
            self.framenumber = (self.framenumber + 1) % len(self.images) #TODO:....they reach the edge.
            self.image = self.images[self.framenumber]

        self.animate()

    def load_images(self):
        self.images = [Spritesheet.get_img(Spritesheet('sprites/cacti-big.png'), 0, 0, 50, 100)]
        for frame in self.images:
            frame.set_colorkey(BLACK)

    def animate(self):
        pass

class BigCactus01(Cactus, pg.sprite.Sprite):

    bCactus_sprite_width = 47
    bCactus_sprite_length = 100



    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (self.bCactus_sprite_width, self.bCactus_sprite_length))

        self.cactus_pos = vec(SCREEN_WIDTH, 657)
        self.cactus_pos.x += 10

    def load_images(self):
        self.images = [Spritesheet.get_img(Spritesheet('sprites/cacti-big.png'), 52, 0 , 99, 100),
                        Spritesheet.get_img(Spritesheet('sprites/cacti-big.png'), 102,0,49, 100),
                        Spritesheet.get_img(Spritesheet('sprites/cacti-big.png'),200, 0, 101, 100 )]
        for frame in self.images:
            frame.set_colorkey(BLACK)

class SmallCactus01(Cactus, pg.sprite.Sprite):

    sCactus_sprite_width = 33
    sCactus_sprite_length = 69

    Cactus_speed = 7
    framenumber = 0

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (self.sCactus_sprite_width, self.sCactus_sprite_length))

        self.cactus_pos = vec(SCREEN_WIDTH, 682)

    def load_images(self):
        self.images = [Spritesheet.get_img(Spritesheet('sprites/cacti-small.png'),0,0,33,69),
                       Spritesheet.get_img(Spritesheet('sprites/cacti-small.png'),36,0,32,69),
                       Spritesheet.get_img(Spritesheet('sprites/cacti-small.png'),69,0,33,69),
                       Spritesheet.get_img(Spritesheet('sprites/cacti-small.png'),137, 0,33,69)]
        for frame in self.images:
            frame.set_colorkey(BLACK)

    def animate(self):
        if self.cactus_pos.x < 0:
            self.framenumber = (self.framenumber + 1) % len(self.images)
            self.image = self.images[self.framenumber]
