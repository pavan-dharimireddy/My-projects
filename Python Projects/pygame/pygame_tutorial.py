import pygame

import random #to make the enemy appear at random places

import math #importing math for calculations

from pygame import mixer # for music or sounds

#initializing pygame
pygame.init()  #whenever you start a game first we have to initialise the pygame

screen = pygame.display.set_mode((800,600)) #creating the screen, and .(dot) is to access the methods of the pygame and we have to add another bracket inside it otherwise it won't work and inside it takes two values width and height  respectively.
#after this statements if you execute the code the screen window pop up only for few seconds because we written the code till there

#to by pass that we create infinite loop
#so we need to add event  quit function
#an event is nothing but anything happening inside the game window

#background = pygame.image.load("background.png")

#background music
mixer.music.load("background.wav")
mixer.music.play(-1) #play the music and -1 is to play in a loop

#title and icon
pygame.display.set_caption("game by @pavan_dahrimireddy") #adding title to my game
icon = pygame.image.load("startup.png") #adding icon , got the icon(must be in png format) from flaticon website and download 32mpx
pygame.display.set_icon(icon) # to display the icon

#adding the player
player = pygame.image.load("spaceship.png") #image from flaticon
playerx = 400 #position of the image (coordinates)
playery = 480 #try different positions
playerx_change = 0

#adding the enemy
   # adding multiple enemy
enemy = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6 #number of enemies

for i in range(num_of_enemies):
    enemy.append(pygame.image.load("ufo.png"))
    enemyx.append(random.randint(0,735)) #making the enemy appear at random places)
    enemyy.append(random.randint(50,150))
    enemyx_change.append(0.3)
    enemyy_change.append(40)

#adding bullets
bullet = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 0.5
bullet_state = "ready" # ready state means we cannot see the bullet on the screen and "fire " means bullet currently moving


#score
score = 0

#adding score on the game window
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)  # to show the font of text and textsize and freesansbold.ttf is free font in pygame and watch video to know how to add external fonts by downloading
textx = 10 #position of the text
texty = 10

#game over
game_over_font = pygame.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    score = font.render("score : " + str(score_value), True, (255,255,255)) # variable.render(text,attributes #(to sshow the text),color)
    screen.blit(score,(x,y))
def players(x,y):
    screen.blit(player,(x,y)) #blit(method) means drawing the image on the screen

def enemies(x,y,i):
    screen.blit(enemy[i],(x,y)) 

def fire_bullet(x,y):
    global bullet_state #to access the bullet_state variable inside this function
    bullet_state = "fire"
    screen.blit(bullet, (x+16,y+10)) #to make sure that the bullet appears at the centre of the spaceship

#game over function
def game_over(x,y):
    game_over_text = game_over_font.render("GAME OVER", True, (225,0,0))
    screen.blit(game_over_text, (200,250))

#collision detection with enemy
def collision(x1,y1,x2,y2):
    distance = math.sqrt((math.pow(x1 - x2, 2))+ (math.pow(y1-y2, 2))) #using the distance formula
    if distance  < 50:
        return True # collision occured

    else:
        return False


#game loop and thing we want to appear continuously we need to add it in infinite loop
run = True
while run:

    #background image
    #screen.blit(background,(0,0))

    #pass #it creates a infinite loop and we cannot close it, because we don't have a event of quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to close the game window by clicking on cross or close button
            run = False
    
        #if keystroke pressed check whether it is right or left
        if event.type == pygame.KEYDOWN: #when any key pressed
            print("keystroke is pressed")
            if event.key == pygame.K_LEFT: # when the pressed key is left arrow key
                print("left arrow is pressed")
                playerx_change = -0.3 #to move left
            if event.key == pygame.K_RIGHT: # when the pressed key is right arrow key
                print("right arrow is pressed")
                playerx_change = 0.3 # to move right
            if event.key == pygame.K_SPACE: #when you press the space key the bullet gonna fire
                if bullet_state is "ready": #without this line if you press spacebar multiple times while firing it again goes in the direction of spaceship
                    bullet_sound = mixer.Sound("laser.wav") #bullet sound
                    bullet_sound.play() # -1 is not there because we don't want in a loop
                    bulletx = playerx  # to avoid the bullet to follow the spaceship direction after firing, and to continue it's straight path after firing
                    fire_bullet(bulletx,bullety)

                
        if event.type == pygame.KEYUP: # when the pressed key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke has been released")
                playerx_change = 0 # to stop




#changing the back ground 
#rgb -- red,green,blue , every colour is made up of these colours
#and (0,0,0) = (red,green,blue) and the value of each colour 0 to 255
#example for pure red (255,0,0) and for light green (0,150,0)
    screen.fill((0,0,0)) #it  is advised to add this line as the first line in while loop
    
    #moving the image left and right
    #playerx += 0.1 #moving towards right
    #playery -= 0.1 #moving towards right diagonally
    #print(playerx,playery)
    playerx += playerx_change

    #adding the boundaries to the image
    if playerx <= 0:
        playerx =0
    elif playerx >=736: # 800 - 64
        playerx = 736

    # enemy  movement 
    for i in range(num_of_enemies):

        #GAME OVER:
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000 # when the enemy hits the spaceship, to make the enemy invisible we are moving it to 2000 pixels
            game_over(200,250)
            break


        enemyx[i]  += enemyx_change[i]
# adding boundries for enemy 
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.3 #when it hits the boundry then it moves back in the same direction
            enemyy[i] +=enemyy_change[i] #so when it hits the left boundry it comes down by 40 coordinates
        elif enemyx[i] >=736: # 800 - 64
            enemyx_change[i] = -0.3
            enemyy[i] +=enemyy_change[i] #so when it hits the right boundry it comes down by 40 coordinates
        #collision
        collision_occurance = collision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision_occurance:
            explosive_sound = mixer.Sound("explosion.wav")
            explosive_sound.play()
            bullety = 480
            bullet_state = "ready"
            score += 1
            score_value += 1
            print("score = ",score )
            enemyx[i] = random.randint(0,735)  #after successfully shot the enemy , new enemy will be generated at random position
            enemyy[i] = random.randint(50,150)
        enemies(enemyx[i],enemyy[i],i) #calling the enemy function

    #Bullet Movement
    if bullety <=0:  #when the bullet crosses the screen it disappears, so we are making it appear in the initial state again
        bullety = 480 
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change #reducing the speed of the bullet
    #addding image in our game

    players(playerx,playery) #calling the players function, to enable the player on the screen

    show_score(textx, texty)
    pygame.display.update() #update the display everytime you add or change anything in the loop







