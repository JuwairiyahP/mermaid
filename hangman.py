import pygame
import os
import math 
import sys
pygame.init()
WIDTH,HEIGHT=800,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("hangman")

def restart():
  con=True
  while con:
    WIN.fill(BLACK)
    title=UGLY_BITE.render("You lost, press R to restart",1,WHITE)
    titlerect=title.get_rect()
    titlerect.center=(WIDTH//2,100)
    WIN.blit(title,titlerect)
    pygame.display.update()
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            os.execl(sys.executable, sys.executable, *sys.argv)

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
PINK=(255,0,127)
#fonts
FREE_TRIAL=pygame.font.Font(r"C:\Users\HP-LAP\Desktop\XI\computer\project\uncracked-font\uncracked.otf",190)
LETTER_FONT=pygame.font.SysFont("comicsans",20)
WORD_FONT=pygame.font.SysFont("comicsans",30)
AIM_FONT=pygame.font.Font(r"C:\Users\HP-LAP\Desktop\XI\computer\project\uncracked-font\nongman.ttf",50)
TITLE_FONT=pygame.font.SysFont("comicsans",30)
UGLY_BITE=pygame.font.Font(r"C:\Users\HP-LAP\Desktop\XI\computer\project\uncracked-font\uglybyte.otf",85)
#button variables
RADIUS=20
GAP=15
letters=[]
startx=round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty=400
A=65
for i in range(26):
  x=startx+GAP*2+((RADIUS*2+GAP)*(i%13))
  y=starty+((i//13)*(GAP+RADIUS*2))
  letters.append([x,y,chr(A+i),True])

#load images
hbg=pygame.image.load("hangmanbg.jpg")
images=[]
for i in range (7):
  image=pygame.image.load(os.path.join("images","hangman"+str(i)+".png"))
  image=pygame.transform.scale(image, (250,250))
  images.append(image)

#game variables
hangmanstat=0
word="ZUGZWANG"
guessed=[]

def start():
  cond=True
  #wanna play
  while cond:
    #intro
    WIN.fill(BLACK)
    title=FREE_TRIAL.render('ARE YOU READY?',1,PINK)
    titlerect=title.get_rect()
    titlerect.center=(WIDTH//2,150)
    WIN.blit(title,titlerect)
    #start
    start=UGLY_BITE.render('Press space to start',1,WHITE)
    startrect=start.get_rect()
    startrect.center=(WIDTH//2,300)
    WIN.blit(start,startrect)
    pygame.display.update()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cond=False

def draw():
  WIN.blit(hbg,[0,0])
  #draw title
  text=AIM_FONT.render("GUESS THE WORD AND USE IT AS THE KEY",1,BLACK)
  WIN.blit(text,(WIDTH/2-text.get_width()/2,20))
  #draw word
  display_word=""
  for letter in word:
    if letter in guessed:
      display_word+=letter+"  "
    else:
      display_word+="_  "
  text=WORD_FONT.render(display_word,1,BLACK)
  WIN.blit(text,(400,200))
  #draw buttons
  for letter in letters:
    x,y,ltr,visible=letter
    if visible:
      pygame.draw.circle(WIN,BLACK,(x,y),RADIUS,3)
      text=LETTER_FONT.render(ltr,1,BLACK)
      WIN.blit(text,(x-text.get_width()/2,y-text.get_width()/2-6))
  #draw hanging thing
  WIN.blit(images[hangmanstat],(100,70))
  pygame.display.update()

def display_message(message):
  pygame.time.delay(1000)
  WIN.blit(hbg,[0,0])
  text=AIM_FONT.render(message,1,BLACK)
  WIN.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_width()/2))
  pygame.display.update()
  pygame.time.delay(3000)
  
def main():
  start()
  global hangmanstat
  FPS=60
  clock=pygame.time.Clock()
  run=True
  while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        run=False
      if event.type==pygame.MOUSEBUTTONDOWN:
        m_x,m_y=pygame.mouse.get_pos()
        for letter in letters:
          x,y,ltr,visible=letter
          if visible:
            dis=math.sqrt((x-m_x)**2+(y-m_y)**2)
            if dis<RADIUS:
              letter[3]=False
              guessed.append(ltr)
              if ltr not in word:
                hangmanstat+=1
    draw()
    won=True
    for letter in word:
      if letter not in guessed:
        won=False
        break
    if won:
      display_message("YOU WIN")
      pygame.quit()
    if hangmanstat==6:
      display_message("YOU LOSE")
      restart()
      
condition=True
while condition:
  main()