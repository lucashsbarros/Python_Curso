'''Faça um programa em Python que abra e reporduza o aúdio de um arquivo MP3'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
