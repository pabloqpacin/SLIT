import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('images/vaporwave.png').convert_alpha()

# Background Sound
mixer.music.load('audio/altingun.wav')
mixer.music.play(-1)
mixer.music.set_volume(0.4)

# Title and Icon
pygame.display.set_caption("Space Invaders by @PabloQuevedoPacin")
icon = pygame.image.load('images/durum.png').convert_alpha()
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/kemal.png').convert_alpha()
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 12

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/tea.png').convert_alpha())
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.2)
    enemyY_change.append(40)

# Bullet
    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving
bulletImg = pygame.image.load('images/gin.png').convert_alpha()
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

# Score // Font
score_value = 0
font = pygame.font.Font('freesansbold.ttf',28)
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf',68)

# Lives
lives_value = 7
font = pygame.font.Font('freesansbold.ttf', 28)
textA = 680 
textB = 10


def show_lives(x,y):
    lives = font.render("Lives: " + str(lives_value), True, (130,240,255))
    screen.blit(lives, (x,y))

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (130,240,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (130,240,255))
    screen.blit(over_text, (200,200))

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x,y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2)) 
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0,0,0))
    
    # Background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it's righ tor left
        if event.type == pygame.KEYDOWN:
#print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.25
#print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.25
#print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('audio/laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
#print("Keystroke has been released")

# Checking for boundaries of player so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

# Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        elif lives_value <= 0:
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('audio/explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
        lives_value -= 1

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change




    player(playerX,playerY)
    show_score(textX,textY)
    show_lives(textA,textB)
    pygame.display.update()
