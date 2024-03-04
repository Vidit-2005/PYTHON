# importing module
import pygame
import random
import tkinter as tk
import math
from pygame import mixer

# initializing module
pygame.init()

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen = pygame.display.set_mode((width, height - 90))

background = pygame.image.load("back.jpg")
mixer.music.load("background.wav")
mixer.music.play(-1)

pygame.display.set_caption("space invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


# classes

class enemy:
    def __init__(self, eimg, ex, ey, e_x, e_y):
        self.enemyi = eimg
        self.enemyx = ex
        self.enemyy = ey
        self.enemy_x = e_x
        self.enemy_y = e_y


class player:
    def __init__(self, pimg, px, py, p_x, p_y):
        self.playerimg = pimg
        self.playerx = px
        self.playery = py
        self.player_x = p_x
        self.player_y = p_y


class bullet:
    def __init__(self, bimg, bx, by, b_x, b_y, bst):
        self.bulletimgage = bimg
        self.bulletx = bx
        self.bullety = by
        self.bullet_x = b_x
        self.bullet_y = b_y
        self.bulletstat = bst


class bullet1:
    def __init__(self, bimg, bx, by, b_x, b_y, bst):
        self.bulletimgage = bimg
        self.bulletx = bx
        self.bullety = by
        self.bullet_x = b_x
        self.bullet_y = b_y
        self.bulletstat = bst


# player & bullet
player1 = player(pygame.image.load("spaceship (1).png"), 750, 650, 0, 0)
pbullet = bullet(pygame.image.load("bullet.png"), 0, 0, 0, 4, 'ready')

# enemy & bullet
enemy1 = enemy(pygame.image.load("alien.png"), random.randint(0, 1020), random.randint(50, 300), 0.8, 40)
enemy2 = enemy(pygame.image.load("alien.png"), random.randint(0, 1020), random.randint(50, 300), 0.8, 40)
enemy3 = enemy(pygame.image.load("alien.png"), random.randint(0, 1020), random.randint(50, 300), 0.8, 40)
enemy4 = enemy(pygame.image.load("alien.png"), random.randint(0, 1020), random.randint(50, 300), 0.8, 40)
enemy5 = enemy(pygame.image.load("alien.png"), random.randint(0, 1020), random.randint(50, 300), 0.8, 40)
enemy6 = enemy(pygame.image.load("alien.png"), random.randint(0, 1020), random.randint(50, 300), 0.8, 40)
ebullet = bullet(pygame.image.load("bullet1.png"), 0, 0, 0, 3, 'ready')
ebullet1 = bullet1(pygame.image.load("bullet1.png"), 0, 0, 0, 3, 'ready')

# score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
texty = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)
won_font = pygame.font.Font("freesansbold.ttf", 64)


# functions

def playerd(x, y):
    screen.blit(player1.playerimg, (x, y))


def show(x, y):
    score1 = font.render("score :" + str(score), True, (255, 200, 100))
    screen.blit(score1, (x, y))


def game_over_t():
    over_text = over_font.render("GAME OVER", True, (25, 200, 10))
    screen.blit(over_text, (600, 350))


def game_won_t():
    won_text = won_font.render("Hura!!! you won the game", True, (25, 200, 11))
    screen.blit(won_text, (400, 350))


def bullet1(x, y):
    pbullet.bulletstat = "fire"
    screen.blit(pbullet.bulletimgage, (x + 16, y + 10))


def enemyd(x, y):
    screen.blit(enemy1.enemyi, (x, y))


def enemyb(x, y):
    ebullet.bulletstat = "fire"
    screen.blit(ebullet.bulletimgage, (x, y))


def enemyb2(x, y):
    ebullet1.bulletstat = "fire"
    screen.blit(ebullet1.bulletimgage, (x, y))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 40:
        return True
    else:
        return False


def icollision(playerx, playery, enemybx, enemyby):
    distance = math.sqrt((math.pow(playerx - enemybx, 2)) + (math.pow(playery - enemyby, 2)))
    if distance < 50:
        return True
    else:
        return False


def icollision2(playerx, playery, enemybx, enemyby):
    distance = math.sqrt((math.pow(playerx - enemybx, 2)) + (math.pow(playery - enemyby, 2)))
    if distance < 50:
        return True
    else:
        return False


# main

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # conencting to keyboard keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.player_x += -1
            if event.key == pygame.K_RIGHT:
                player1.player_x += 1
            if event.key == pygame.K_UP:
                player1.player_y += -1
            if event.key == pygame.K_DOWN:
                player1.player_y += 1
            if event.key == pygame.K_SPACE:
                # fire1(playerx,playery)
                if pbullet.bulletstat == "ready":
                    pbullet.bulletx = player1.playerx
                    pbullet.bullety = player1.playery
                    bullet1(pbullet.bulletx, pbullet.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
            if event.key == pygame.K_a:
                if ebullet.bulletstat == "ready":
                    ebullet.bulletx = enemy1.enemyx
                    ebullet.bullety = enemy1.enemyy
                    enemyb(ebullet1.bulletx, ebullet1.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
            if event.key == pygame.K_q:
                if ebullet.bulletstat == "ready":
                    ebullet1.bulletx = enemy2.enemyx
                    ebullet1.bullety = enemy2.enemyy
                    enemyb2(ebullet1.bulletx, ebullet1.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
            if event.key == pygame.K_w:
                if ebullet.bulletstat == "ready":
                    ebullet.bulletx = enemy3.enemyx
                    ebullet.bullety = enemy3.enemyy
                    enemyb(ebullet1.bulletx, ebullet1.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
            if event.key == pygame.K_e:
                if ebullet.bulletstat == "ready":
                    ebullet.bulletx = enemy4.enemyx
                    ebullet.bullety = enemy4.enemyy
                    enemyb(ebullet.bulletx, ebullet.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
            if event.key == pygame.K_s:
                if ebullet1.bulletstat == "ready":
                    ebullet1.bulletx = enemy5.enemyx
                    ebullet1.bullety = enemy5.enemyy
                    enemyb2(ebullet.bulletx, ebullet.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
            if event.key == pygame.K_d:
                if ebullet1.bulletstat == "ready":
                    ebullet1.bulletx = enemy6.enemyx
                    ebullet1.bullety = enemy6.enemyy
                    enemyb2(ebullet.bulletx, ebullet.bullety)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.player_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1.player_y = 0

    # player movement
    player1.playerx += player1.player_x
    player1.playery += player1.player_y

    if player1.playerx <= 0:
        player1.playerx = 0
    elif player1.playerx >= 1485:
        player1.playerx = 1485
    if player1.playery <= 0:
        player1.playery = 0
    elif player1.playery >= 706:
        player1.playery = 706

    if pbullet.bullety <= 0:
        pbullet.bullety = 766
        pbullet.bulletstat = "ready"
    if pbullet.bulletstat == "fire":
        bullet1(pbullet.bulletx, pbullet.bullety)
        pbullet.bullety -= pbullet.bullet_y

    # enemy movement
    enemy1.enemyx += enemy1.enemy_x
    enemy2.enemyx += enemy2.enemy_x
    enemy3.enemyx += enemy3.enemy_x
    enemy4.enemyx += enemy4.enemy_x
    enemy5.enemyx += enemy5.enemy_x
    enemy6.enemyx += enemy6.enemy_x

    if enemy1.enemyx <= 0:
        enemy1.enemy_x = 0.5
        enemy1.enemyy += enemy1.enemy_y
    elif enemy1.enemyx >= 1500:
        enemy1.enemy_x = -0.5
        enemy1.enemyy += enemy1.enemy_y
    if enemy2.enemyx <= 0:
        enemy2.enemy_x = 0.5
        enemy2.enemyy += enemy2.enemy_y
    elif enemy2.enemyx >= 1500:
        enemy2.enemy_x = -0.5
        enemy2.enemyy += enemy2.enemy_y
    if enemy3.enemyx <= 0:
        enemy3.enemy_x = 0.5
        enemy3.enemyy += enemy3.enemy_y
    elif enemy3.enemyx >= 1500:
        enemy3.enemy_x = -0.5
        enemy3.enemyy += enemy3.enemy_y
    if enemy4.enemyx <= 0:
        enemy4.enemy_x = 0.5
        enemy4.enemyy += enemy4.enemy_y
    elif enemy4.enemyx >= 1500:
        enemy4.enemy_x = -0.5
        enemy4.enemyy += enemy4.enemy_y
    if enemy5.enemyx <= 0:
        enemy5.enemy_x = 0.5
        enemy5.enemyy += enemy5.enemy_y
    elif enemy5.enemyx >= 1500:
        enemy5.enemy_x = -0.5
        enemy5.enemyy += enemy5.enemy_y
    if enemy6.enemyx <= 0:
        enemy6.enemy_x = 0.5
        enemy6.enemyy += enemy6.enemy_y
    elif enemy6.enemyx >= 1500:
        enemy6.enemy_x = -0.5
        enemy6.enemyy += enemy6.enemy_y

    # enemey bullet repositioning
    if ebullet.bullety >= 766:
        ebullet.bullety = 0
        ebullet.bulletstat = "ready"
    if ebullet.bulletstat == "fire":
        enemyb(ebullet.bulletx, ebullet.bullety)
        ebullet.bullety += ebullet.bullet_y
    if ebullet1.bullety >= 766:
        ebullet1.bullety = 0
        ebullet1.bulletstat = "ready"
    if ebullet1.bulletstat == "fire":
        enemyb2(ebullet1.bulletx, ebullet1.bullety)
        ebullet1.bullety += ebullet.bullet_y

    # enemy collision
    collision = iscollision(enemy1.enemyx, enemy1.enemyy, pbullet.bulletx, pbullet.bullety)
    if collision:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        pbullet.bullety = player1.playery
        pbullet.bulletstat = "ready"
        score += 1
        enemy1.enemyx = random.randint(0, 1500)
        enemy1.enemyy = random.randint(50, 400)
    collision2 = iscollision(enemy2.enemyx, enemy2.enemyy, pbullet.bulletx, pbullet.bullety)
    if collision2:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        pbullet.bullety = player1.playery
        pbullet.bulletstat = "ready"
        score += 1

        enemy2.enemyx = random.randint(0, 1500)
        enemy2.enemyy = random.randint(50, 400)
    collision3 = iscollision(enemy3.enemyx, enemy3.enemyy, pbullet.bulletx, pbullet.bullety)
    if collision3:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        pbullet.bullety = player1.playery
        pbullet.bulletstat = "ready"
        score += 1
        enemy3.enemyx = random.randint(0, 1500)
        enemy3.enemyy = random.randint(50, 400)
    collision4 = iscollision(enemy4.enemyx, enemy4.enemyy, pbullet.bulletx, pbullet.bullety)
    if collision4:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        pbullet.bullety = player1.playery
        pbullet.bulletstat = "ready"
        score += 1
        enemy4.enemyx = random.randint(0, 1500)
        enemy4.enemyy = random.randint(50, 400)
    collision5 = iscollision(enemy5.enemyx, enemy5.enemyy, pbullet.bulletx, pbullet.bullety)
    if collision5:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        pbullet.bullety = player1.playery
        pbullet.bulletstat = "ready"
        score += 1
        enemy5.enemyx = random.randint(0, 1500)
        enemy5.enemyy = random.randint(50, 400)
    collision6 = iscollision(enemy6.enemyx, enemy6.enemyy, pbullet.bulletx, pbullet.bullety)
    if collision6:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        pbullet.bullety = player1.playery
        pbullet.bulletstat = "ready"
        score += 1
        enemy6.enemyx = random.randint(0, 1500)
        enemy6.enemyy = random.randint(50, 400)

    # player collision
    collision = icollision(player1.playerx, player1.playery, ebullet.bulletx, ebullet.bullety)
    collisiony = icollision(player1.playerx, player1.playery, ebullet1.bulletx, ebullet1.bullety)
    collision1 = icollision2(player1.playerx, player1.playery, enemy1.enemyx, enemy1.enemyy)
    collision2 = icollision2(player1.playerx, player1.playery, enemy2.enemyx, enemy2.enemyy)
    collision3 = icollision2(player1.playerx, player1.playery, enemy3.enemyx, enemy3.enemyy)
    collision4 = icollision(player1.playerx, player1.playery, enemy4.enemyx, enemy4.enemyy)
    collision5 = icollision(player1.playerx, player1.playery, enemy5.enemyx, enemy5.enemyy)
    collision6 = icollision(player1.playerx, player1.playery, enemy6.enemyx, enemy6.enemyy)
    if collision:
        ebullet.bulletstat = "ready"
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collisiony:
        ebullet.bulletstat = "ready"
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collision1:
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collision2:
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collision3:
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collision4:
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collision5:
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
    if collision6:
        score -= 2
        player1.playerx = 775
        player1.playery = 600
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()

    # extra condition for gaming experience
    if enemy1.enemyy >= 636 or enemy2.enemyy >= 636 or enemy3.enemyy >= 636 or enemy4.enemyy >= 636 or enemy5.enemyy >= 636 or enemy6.enemyy >= 636:
        enemy1.enemyy = 2000
        enemy2.enemyy = 2000
        enemy3.enemyy = 2000
        enemy4.enemyy = 2000
        enemy5.enemyy = 2000
        enemy6.enemyy = 2000
        game_over_t()

    # score limit
    if score < -4:
        player1.playery = 2000
        player1.playerx = 2000
        game_over_t()
    if score > 11:
        enemy1.enemyy = -2000
        enemy1.enemyx = -2000
        enemy2.enemyy = -2000
        enemy2.enemyx = -2000
        enemy3.enemyy = -2000
        enemy3.enemyx = -2000
        enemy4.enemyy = -2000
        enemy4.enemyx = -2000
        enemy5.enemyy = -2000
        enemy5.enemyx = -2000
        enemy6.enemyy = -2000
        enemy6.enemyx = -2000
        game_won_t()

    # displaying element
    playerd(player1.playerx, player1.playery)
    show(textx, texty)
    enemyd(enemy3.enemyx, enemy3.enemyy)
    enemyd(enemy2.enemyx, enemy2.enemyy)
    enemyd(enemy1.enemyx, enemy1.enemyy)
    enemyd(enemy4.enemyx, enemy4.enemyy)
    enemyd(enemy5.enemyx, enemy5.enemyy)
    enemyd(enemy6.enemyx, enemy6.enemyy)
    pygame.display.update()
pygame.quit()
quit()