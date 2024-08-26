import pygame
import math
import os
import sys
from pygame import mixer
pygame.init()
mixer.init()
sound=pygame.mixer.Sound('bgm.mp3')
sound.play()
WIDTH,HEIGHT=800,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("introduction")
#images
images=[]
for j in range (16):
    image=pygame.image.load(os.path.join("images","intro"+str(j)+".png"))
    image=pygame.transform.scale(image, (800,500))
    images.append(image)
#fonts
#colours
WHITE=(255,255,255)
#----
FPS=60
clock=pygame.time.Clock()
introrun=True
def draw1():
  draw1con=True
  i=0
  while draw1con==True:
    while i<16:
        WIN.fill(WHITE)
        WIN.blit(images[i],(0,0))
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    i=17
                    draw1con=False
                    pygame.quit()
                if event.key == pygame.K_c:
                    i+=1
                    break
while introrun:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_s:
              introrun=False
              break    
    draw1()
    introrun=False
#-------------------------------------------------------------------------
import pygame 
pygame.init()
WIDTH,HEIGHT=800,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("hangman")

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
PINK=(255,0,127)
#sound effect
def key():
    mixer.music.load("door-lock-1.mp3")
    pygame.time.delay(2000)
    mixer.music.play()
#fonts
FREE_TRIAL=pygame.font.Font(r"C:\Users\Juwairiyah\OneDrive\Desktop\cs\final project\project\uncracked-font\uncracked.otf",190)
LETTER_FONT=pygame.font.SysFont("comicsans",20)
WORD_FONT=pygame.font.SysFont("comicsans",30)
AIM_FONT=pygame.font.Font(r"C:\Users\Juwairiyah\OneDrive\Desktop\cs\final project\project\uncracked-font\nongman.ttf",50)
TITLE_FONT=pygame.font.SysFont("comicsans",30)
UGLY_BITE=pygame.font.Font(r"C:\Users\Juwairiyah\OneDrive\Desktop\cs\final project\project\uncracked-font\uglybyte.otf",85)
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
  afterwinhg=AIM_FONT.render("YOU USE THE KEY AND THE GATE UNLOCKS",1,BLACK)
  WIN.blit(afterwinhg,(50,260))
  key()
  pygame.display.update()
  pygame.time.delay(3000)
  
def main():
  start()
  global hangmanstat
  FPS=60
  clock=pygame.time.Clock()
  run=True
  while run:
    global cond
    global condition
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
      cond=False
      condition=False
      run=False
      pygame.quit()
    if hangmanstat==6:
      pygame.time.delay(1000)
      pygame.quit()
      print("YOU COULDN'T GET PASS THE GATE WITHOUT THE KEY,TRY AGAIN NEXT TIME :)")
      sys.exit()
      
condition=True
while condition:
  main()
  conition=False
#-------------------------------------------------------------------------
pygame.init()
#trollimg
trollimg=[]
for j in range (3):
    image=pygame.image.load(os.path.join("images","troll"+str(j)+".png"))
    image=pygame.transform.scale(image, (800,500))
    trollimg.append(image)
trollrun=True
WIN = pygame.display.set_mode((800,500))
def draw2():
  draw2con=True
  i=0
  while draw2con==True:
    while i<3:
        WIN.fill(WHITE)
        WIN.blit(trollimg[i],(0,0))
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    i=4
                    draw2con=False
                    pygame.quit()
                if event.key == pygame.K_c:
                    i+=1
                    break
while trollrun:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_s:
              trollrun=False
              break
    mixer.music.load("witch.mp3")
    mixer.music.play()
    draw2()
    trollrun=False
#-------------------------------------------------------------------------
import pygame
import os
pygame.init()

from pygame import mixer
FREE_TRIAL=pygame.font.Font(r"C:\Users\Juwairiyah\OneDrive\Desktop\cs\final project\project\uncracked-font\uncracked.otf",100)

WIN = pygame.display.set_mode((800,600)) 
pygame.display.update()
bg_img = pygame.image.load('piano bg.jpg')
bg_img = pygame.transform.scale(bg_img, (800,600))
mc_piano = ''
def dm_piano(message):
  pygame.time.delay(1000)
  WIN.fill((0,0,0))
  text = FREE_TRIAL.render(message,1,(210,105,30))
  WIN.blit(text,(110,220))
  pygame.display.update()
  mixer.music.load("snore.mp3")
  mixer.music.play()
  pygame.time.delay(8000)
running = True
while running:
    WIN.fill((153,50,204))   
    WIN.blit(bg_img, (0,0))
    pygame.display.update() 
    piano = {1:'mssmrdrmrdd'}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                do = mixer.Sound('do.wav')
                do.play()
                mc_piano+='d'
            if event.key == pygame.K_r:
                re = mixer.Sound('re.wav')
                re.play()
                mc_piano+='r'
            if event.key == pygame.K_m:
                mi = mixer.Sound('mi.wav')
                mi.play()
                mc_piano+='m'
            if event.key == pygame.K_f:
                fa = mixer.Sound('fa.wav')
                fa.play()
                mc_piano+='f'
            if event.key == pygame.K_s:
                sol = mixer.Sound('sol.mp3')
                sol.play()
                mc_piano+='s'
            if event.key == pygame.K_l:
                la = mixer.Sound('la.wav')
                la.play()
                mc_piano+='l'
            if event.key == pygame.K_t:
                ti = mixer.Sound('ti.wav')
                ti.play()
                mc_piano+='t'
            if event.key == pygame.K_o:
                do = mixer.Sound('do 2.wav')
                do.play()
                mc_piano+='o'       
            if event.key == pygame.K_1:
                if mc_piano == piano[1]:
                    dm_piano("GREAT! HE HAS SLEPT")
                    running=False
                    pygame.quit()
                else:
                    dm_piano("OOPS! YOU SLEPT INSTEAD")
                    pygame.quit()
                    print("THE TROLL WAS UPSET WITH YOUR INTENTIONS,TRY AGAIN NEXT TIME :)")
                    sys.exit()
                running=False
#-------------------------------------------------------------------------             
final1=pygame.image.load("final1.jpeg")
final1=pygame.transform.scale(final1, (800,500))
final2=pygame.image.load("final2.jpeg")
final2=pygame.transform.scale(final2, (800,500))
final3=pygame.image.load("final3.jpeg")
final3=pygame.transform.scale(final3, (800,500))
final4=pygame.image.load("final4.jpeg")
final4=pygame.transform.scale(final4, (800,500))
final5=pygame.image.load("final5.jpeg")
final5=pygame.transform.scale(final5, (800,500))
final6=pygame.image.load("final6.jpeg")
final6=pygame.transform.scale(final6, (820,500))
finalimages=[final1,final2,final3,final4,final5,final6]
pygame.init()
WIN = pygame.display.set_mode((800,500))
WIN.fill((0,0,0))
finalsound = []
finalsound.append(pygame.mixer.Sound('running.mp3'))
finalsound.append(pygame.mixer.Sound('pant.mp3'))
for sound in finalsound:
    sound.play()
    sound.play()
WIN.blit(finalimages[0],(0,0))
pygame.display.update()
pygame.time.delay(17000)
WIN.blit(finalimages[1],(0,0))
pygame.display.update()
pygame.time.delay(4000)
WIN.blit(finalimages[2],(0,0))
pygame.display.update()
mixer.music.load("movement.mp3")
mixer.music.play()
pygame.time.delay(13000)
mixer.music.load("movement.mp3")
mixer.music.play()
pygame.time.delay(13000)
mixer.music.load("movement.mp3")
mixer.music.play()
pygame.time.delay(2000)
WIN.blit(finalimages[3],(0,0))
pygame.display.update()
mixer.music.load("movement.mp3")
mixer.music.play()
pygame.time.delay(10000)
mixer.music.load("movement.mp3")
mixer.music.play()
pygame.time.delay(10000)
mixer.music.load("come.mp3")
mixer.music.play()
pygame.time.delay(6000)
pygame.mixer.music.fadeout
WIN.blit(finalimages[4],(0,0))
pygame.display.update()
pygame.time.delay(5000)
WIN.blit(finalimages[5],(-10,0))
pygame.display.update()
pygame.time.delay(7000)

pygame.quit()
#-------------------------------------------------------------------------
#INSTRUCTIONS
print('''HELLO USER
Congrats on reaching the final level of the game
This level comprises of convincing the mermaid with appropriate dialogues:
1)Make sure your choice is just the number 1/2/3
2)Program is case sensitive so make sure to enter the inputs in the right manner
3)The program is under a limit, if your choices are impolite it might go over the limit and you will lose
4)Conversations written in brackets are from the main character Ruth ''')
ok=input("If you are clear with the instructions, press 'o' to continue:")
#CONVO CODE
def convolose():
    if v>6:
        print("Your dialogue choice was poor, it seems to have pissed the mermaid over the limit \n --YOU LOSE--")
        sys.exit()
if ok=='o':
    v=0
    #if v>6 u lose
    print("___________\nVanessa: Seriously? A human? Again? \n (She is trying to speak with a British accent. Did she learn it from someone? But what did she mean by 'again'? Should I ask right away?)")
    one=input("1) Introduce and then ask \n2) What do you mean 'again'? \n3) You've got a funny accent \n:")
    print("__________________________________________________________________")
    if one=='1':
        print("Hello Miss Mermaid! My name is Ruth. I come from dash village. Is everything all right? What did you mean by 'again'? \nThe mermaid looks at Ruth. Her sharp eyes fixed on Ruth. And replies, \nVanessa: Well, hello, Ruth! This is a relief. At least this time I'll be dealing with someone polite. \n*mumbles to herself* Polite enough to greet a person they meet for the first time.")
    elif one=='2':
        print("The mermaid raised her left eyebrow as someone in disbelief. She looked at her uninvited guest and \nVanessa:  Do I know you? \n Ruth: Ah! Hello Miss Mermaid, I am Ruth.")
        v+=1
    elif one=='3':
        print("The mermaid looks annoyingly at Ruth. \nVanessa: See! Humans are all the same.. What a rude bunch of creatures! Well, let me teach you, illmannered brat! \nYou can start showing respect by introducing yourself. \nRuth: Oh! Hello Miss Mermaid, I am Ruth.")
        v+=2
    print("___________\nNevertheless, why do we have to suffer because of humans? You create new things to make life easier but then dump all the after-effects on those around you? Why have you come? You have already exploited all of your resources, and now you are here to destroy my home? Is that why you are here? This is like, what, the 150th time? Or 51?  Ha! I lost count after the 100th human tried to barge in like they owned this place. \n(Exploited? Destroy her home? Humans tried to barge in? What is she talking about? Bernard told me countless men have tried to find the mermaid and solve this mess, but nobody returned alive. Did they even try talking to her or were they here with a different motive?)")
    two=input("1) What are you talking about? \n2) Miss Mermaid, I don't understand. Humans tried to destroy your home? \n3) I am here to ask you to stop monopolizing this beautiful place.\n:")
    print("__________________________________________________________________")
    if two=='1':
        print("The mermaid gave out a big sigh \nVanessa: I am talking about the injustice the other beings are going through because you humans have monopolized everything around you, leaving nothing for the others. Right now, you are here to take me hostage and have this place all to yourselves, am I right?")
        v+=1
    elif two=='2':
        print("The mermaid stared at Ruth without a change in expression and replied \nVanessa: Yes, I know you are here like your peers to take me hostage and have this place all to yourselves, Right?")
    elif two=='3':
        print("The mermaid scoffed as if in disbelief and said, \nMermaid: It is funny how you blame me for monopolizing my home now. After putting my guard troll to sleep, trespassed into my house, and now you have the nerve to accuse me? You are here to take me hostage aren't you? ")
        v+=2
    print("(What is Venus talking about? Does she not recognize me? I even introduced myself. \nWell at least, her temper is still the same. * giggles* )")
    print("___________\nVanessa: What? Now you find this funny? Did you think introducing yourself as someone I used to know shall get you any closer to me? Human, leave while I ask you to.")
    three=input("1)Why should I leave? This land belongs to everyone, so stop whining.Also quit making people vanish just because you don't like them. \n2) No, I shan't till I convince you to stop making people disappear. \n3) I will leave when I want to. Don't tell me what to do.\n:")
    print("__________________________________________________________________")
    if three=='1':
        print("Vanessa: Oh, the nerve! To call this land yours.")
        v+=1
    elif three=='2':
        print("Vanessa: Now you are really annoying me!")
    elif three=='3':
        print("Vanessa: This cheeky little..{Vanessa bites her tongue}..Listen human, you are testing my patience.")
        v+=2
    print("(uh-oh Venus looks pissed)")
    print("___________\nVanessa: And what's this about me making people disappear. FYI, I am a mermaid, not a magician. I indeed get irritated every time a human trespasses my land. But I have never hurt anyone unless they threaten me to leave my home. And tell that king of yours that I will not fall for his deceits anymore. Even if he sends MY Ruth here, I do not intend to hand over my land as he wishes. I will not trust her or any other humans ever again. This land belongs to me and the creatures living here. Ask him to get his daughter something that doesn't have an owner. Now that you've cleared your doubts, prepare to leave. I don't wish to waste my precious time on you anymore. ")
    print("(The king wanted her land? For the princess? And she wouldn't trust me ... again? Good lord! This is the real reason why she left not because of her specie, my kind were secretly demanding her place without me knowing!)")
    four=input("1)Venus, please let me explain. I am sure this is all a misunderstanding \n2)How could you insult the royal family Venus?! Bernard was right. Mermaids are ungrateful! \n3) Venus i guess there has been a misunderstanding\n:")
    print("__________________________________________________________________")
    if four=='1':
        print("Vanessa: You- \nVanessa opened her mouth to speak, then she suddenly stopped and looked at Ruth with eyes wide open. \nVanessa: You! That name...she gave me that name. Ruth?")
    elif four=='2':
        v+=3
        convolose()
        print("Vanessa looked furiously at Ruth and then shouted,\nVanessa: Well, guess I am ungrateful. So YOU SHOULD LEAVE NOW! Before you get more annoyed by my \"ungratefulness\"- \nShe suddenly stopped, her eyes wide open \nVanessa: That name...Are you...")
    
    elif four=='3':
        v+=1
        convolose()
        print("Vanessa: Yeah sure, misunderstand- \nShe suddenly stopped, her eyes wide open \nVanessa: Are you...")
    print("___________\nVanessa: Ruth? Is that really you? You...Well...You do look like her!! \nVanessa looked at her. A slight smile escaped her mouth. But she quickly hid it with her hand. \nAfter she regained her stern poise, she spoke in a soft yet firm manner,\nVanessa: Well, you have finally come! I thought the king would never let me see you again. But I assume he is desperate to have this land that he sent you? Even if it's you, Ruth, I cannot hand over this place.")
    five=input("1)Why can't you? I think this is the best for both of us. \n2)How foolish of you to not accept the king's offer! I am sure he would pay you handsomely. \n3)I understand, Venus.\n:")
    print("__________________________________________________________________")
    if five=='1':
        v+=1
        convolose()
        print("Vanessa: You don't understand Ruth. The king wants to monopolize the land. He will not allow the common folks to enter this place once it becomes the princess's private property.\nRuth: Now I understand..")
    elif five=='2':
        v+=3
        convolose()
        print("Venesa: Ruth! Wake up! They are all fooling you! The king wants to monopolize this land. He will not allow the common folks to enter this place once it becomes the princess's private property.\nRuth: Now I understand..")
    elif five=='3':
        print()
    print()
    print("___________\nRuth: The king asked for this land because the princess wanted this place all for herself. Coincidently or not, I and you became friends. Later when you found out the king's desire to own this place, you thought I plotted with them to get this land and that is why I befriended you. Is that right?")
    print("Vanessa: Well, that's-")
    print("Ruth: It's alright Venus! I told you I am not here for the land. I just...thought we could be friends again. Friendship is built on respect and trust.  Even if you respect someone but don't trust them, the friendship will crumble. \nAnyways, you said that you haven't hurt any innocent person. Then I shall take this matter to the townspeople and the king. Don't worry I will make sure that no one tries to snatch your home from you again. Now, I will leave you to yourself. Goodbye Venus.")
    theend=input("---THE GAME HAS ENDED,YOU WIN..if you want to know the ending press e--- \n:")
    if theend=='e':
        print("__________________________________________________________________")
        print('''Vanessa's POV:
        I was really happy when I made a human friend for the first time. Even though my mother warned me that humans, the most intellectually capable beings on earth who held the power of invention, are the most dangerous beings. Though, I never paid her any heed. 
        I loved the new friend I made. I liked her long and silky purple hair, big golden eyes that were always in search of something adventurous and the way she always talked about the human world whenever she visited me. She always looked bright and cheerful even when she was going through a hard time. Nevertheless, sometimes, she looks so lonely as the moon. Moon-like, I thought.    
        I still don't know how she found this place though. All I knew was I liked being her friend until...until I overheard that big old bearded man talking to someone about building a greenhouse around my home for the princess, in return for a place to stay in the human world with Ruth. I was devastated. "I considered Ruth my little sister, yet...yet she betrayed me!?! ", was what I thought. I was hurt, not by the thought of my home being subjugated but by Ruth's betrayal.   
        But, is she saying that she didn't know any of this? Ruth was innocent? I...I didn't even bother to clarify it with Ruth, and jumped to my own conclusion? 
        
    *flashback *
Ruth: Venus, my mother told me that it takes years to build trust but seconds to break it and forever to repair, so you must always trust me no matter what, okay?
        
    To the present:
    {Ruth turns back and starts walking}
    Vanessa: Ruth wait!
    {Ruth stops and turns back}
    Vanessa: Why...do you always call me Venus? 
    {Suddenly silence cuts through. THE AIR WAS STILL COTTONY WITH FOG. The silence is broken by Ruth's reply}
    Ruth: Remember the time you called me the Moon?  Venus is the second brightest natural object in the night sky after the moon. That's why.
        
{Ruth turns towards the exit and walks away as Vanessa watches her friend fade into the mist}
        ________THE END______''') 