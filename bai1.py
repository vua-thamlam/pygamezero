import random
import pgzrun 
from random import randint

WIDTH =800
HEIGHT=600
game_over=False

ship= Actor('playership1_blue')
ship.x=370
ship.y=550

meto=Actor('meteorgrey_big1.png')
meto.x=300
meto.y=0

gem=Actor('gemblue')
gem.x=200
gem.y=0
score = 0 
def update():
    global score ,game_over

    gem.y=gem.y+4+score/4
    meto.y=meto.y+4
    if gem.y>600:
        gem.y=0
    if meto.y>600:
        meto.y=0

    if gem.colliderect(ship):
        gem.x=random.randint(20,780)
        gem.y=0
        score=score + 1
        sounds.epe.play()

    if meto.colliderect(ship):
        game_over=True
        sounds.gameover.play()
         
        
def on_mouse_move(pos,rel,buttons):
    ship.x=pos[0]
    ship.y=pos[1]
def draw():
    screen.fill((0,0,0))
    if game_over:
        screen.draw.text('game over',(360,300),color=(255,255,255),fontsize=60)
        screen.draw.text('Final score:'+str(score),(360,350),color=(255,0,255),fontsize=80)
    else:
      ship.draw()
      gem.draw()
      meto.draw()
      screen.draw.text('score:' + str(score),(15,10),color=(255,255,255),fontsize=30)
    
pgzrun.go()