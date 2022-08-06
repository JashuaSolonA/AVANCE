import pygame

pygame.mixer.init(frequency=44100)

pygame.mixer.music.load("Grabación.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

VENTANA = pygame.display.set_mode()
pygame.display.set_caption('Musica')
Imagen = pygame.image.load('LA.png')
pygame.display.set_icon(Imagen)

sonidomute = pygame.image.load('LA.png')
sonido1 = pygame.image.load('LA.png')
sonido2 = pygame.image.load('LA.png')
sonido3 = pygame.image.load('LA.png')
sonidomax = pygame.image.load('LA.png')

ejecuta = True

while ejecuta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_2] and pygame.mixer.music.get_volume > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
        
    elif keys[pygame.K_2] and pygame.mixer.music.get_volume() == 0.0:
        VENTANA.blit(sonidomute, (850,25))

    if keys[pygame.K_3] and pygame.mixer.music.get_volume < 0.4:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        
    elif keys[pygame.K_3] and pygame.mixer.music.get_volume() == 0.4:
        VENTANA.blit(sonidomax, (850,25))

    elif keys[pygame.K_1]:
        pygame.mixer.music.set_volume(0.0)
        VENTANA.blit(sonidomute, (850, 25))

    elif keys[pygame.K_4]:
        pygame.mixer.music.set_volume(0.4)
        VENTANA.blit(sonidomax, (850, 25))