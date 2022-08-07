import pygame
import sys

pygame.mixer.init(frequency=44100)

pygame.mixer.music.load("ringtones-super-mario-bros.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

size = 800, 600

VENTANA = pygame.display.set_mode(size)
pygame.display.set_caption('Musica')
Imagen = pygame.image.load('mariobros.png')
pygame.display.set_icon(Imagen)

fondo = pygame.image.load('mariobros_redimensionada.png')
VENTANA.blit(fondo,(0,0))

ejecuta = True

while ejecuta:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_2]:
        pygame.mixer.music.set_volume(0.25)

    elif keys[pygame.K_3]:
        pygame.mixer.music.set_volume(0.50)
    
    elif keys[pygame.K_1]:
        pygame.mixer.music.set_volume(0.0)

    elif keys[pygame.K_4]:
        pygame.mixer.music.set_volume(1.0)

pygame.quit()