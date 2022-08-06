import pygame

pygame.mixer.init(frequency=44100)
pygame.mixer.music.load("Grabación.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)



VENTANA = pygame.display.set_mode()
pygame.display.set_caption('Musica')
Imagen = pygame.image.load('LA.png')
pygame.display.set_icon(Imagen)
ejecuta = True

while ejecuta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
    
    keys=pygame.key.get_pressed()



    if keys[pygame.K_1]:
        pygame.mixer.music.set_volume(0.0)

    elif keys[pygame.K_2]:
        pygame.mixer.music.set_volume(0.4)