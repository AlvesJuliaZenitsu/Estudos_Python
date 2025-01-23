#Faça um programa que abra e reproduza o áudio de um arquivo MP3


import pygame
import time

pygame.init()
pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.load('Tste.mp3')
pygame.mixer.music.play()
time.sleep(10)
pygame.event.wait()

#FUNCIONOOOOOOOOOOOOOOU AAAAAAAAAAAAAAAEEEEEEEEEEEEEEEEEEEEEEE
#Graças ao time