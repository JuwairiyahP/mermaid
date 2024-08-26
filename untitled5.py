import pygame
from pygame import mixer
pygame.init()
WIN = pygame.display.set_mode((800,500))
WIN.fill((0,0,0))
pygame.display.update()

mixer.music.load("movement.mp3")
mixer.music.play()
pygame.time.delay(5000)
mixer.music.load("come.mp3")
mixer.music.play()
pygame.time.delay(5000)
pygame.quit()