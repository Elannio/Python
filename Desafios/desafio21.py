# Faça um programa que abra e reproduza o áudio de um arquivo mp3

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()