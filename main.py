import pygame
pygame.init()
pygame.mixer.music.load('01- Cristo, meu Mestre.mp3')
pygame.mixer.music.play(loops=0,start=0.1,fade_ms=99)
pygame.event.wait()