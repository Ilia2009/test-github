#Создай собственный Шутер!

from pygame import *
from random import *
a = 0
counter_missings = 0
 
 
init()
 
window = display.set_mode((700,500))
display.set_caption('Shooter')
 
clock = time.Clock()
 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
 
 
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed = 5, w = 65, h = 65):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
 
    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Rocket(GameSprite):
    def move(self):
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
 
class Ufo(GameSprite):
    def update(self):
        global counter_missings
        self.rect.y += self.speed
        if self.rect.y >= 500:
            counter_missings += 1
            self.rect.y = -50
            self.rect.x = randint(10, 630)
 
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -50
            self.rect.x = randint(10, 630) 
class Big(GameSprite):
    def boss(self):
        self.rect.y += self.speed
    




background = transform.scale(image.load('galaxy.jpg'), (700,500))
rocket = Rocket('rocket.png', 300, 430, 10)
ufo1 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo2 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo3 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo4 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo5 = Ufo('ufo.png', randint(10, 630), 0, 3)
 
asteroid1 = Asteroid('asteroid.png', randint(10,630), 0, 3)
asteroid2 = Asteroid('asteroid.png', randint(10,630), 0, 3)
 
asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)


ufos = sprite.Group()
ufos.add(ufo1)
ufos.add(ufo2)
ufos.add(ufo3)
ufos.add(ufo4)
ufos.add(ufo5)

big1 = Big('big.png', 200, 20, 3, 200, 200)



bullets = sprite.Group()
 
game = True
while game:
    keys = key.get_pressed()
    if keys[K_w]:
        bullets.add(Bullet('bullet.png', rocket.rect.centerx-7, rocket.rect.top, 30, 15, 30))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullets.add(Bullet('bullet.png', rocket.rect.centerx-7, rocket.rect.top, 30, 15, 30))
            '''if a == 25:'''
    #printing
    window.blit(background, (0,0))
    rocket.paint()
    ufos.draw(window)
    bullets.draw(window)
    asteroids.draw(window)
    big1.paint()
    #moves
    rocket.move()
    ufos.update()
    bullets.update()
    asteroids.update()
    #collisions
    
    if sprite.groupcollide(bullets, ufos, True, True):
        a += 1
        print(a)
    if len(ufos) < 5:
        ufos.add(Ufo('ufo.png', randint(10, 630), 0, 3))
 
    sprite.spritecollide(rocket, ufos, True)
 
    display.update()
    clock.tick(60)