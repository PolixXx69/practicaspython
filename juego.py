import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
pantalla_ancho = 800
pantalla_alto = 600
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))

# Configuración del personaje
personaje_ancho = 50
personaje_alto = 50
personaje_x = pantalla_ancho / 2
personaje_y = pantalla_alto / 2
velocidad = 5
gravedad = 1

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el personaje
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personaje_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        personaje_x += velocidad
    if teclas[pygame.K_UP] and personaje_y == pantalla_alto / 2:
        personaje_y -= 20
        gravedad = -20
    personaje_y += gravedad
    gravedad += 1
    if personaje_y > pantalla_alto / 2:
        personaje_y = pantalla_alto / 2
        gravedad = 0

    # Dibujar el personaje
    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (255, 0, 0), (personaje_x, personaje_y, personaje_ancho, personaje_alto))
    pygame.display.flip()
    pygame.time.Clock().tick(60)


