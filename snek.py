import pygame

ancho = 500
altura = 500

def main():
    x = 40
    y = 40

    velocidad = 9

    pygame.init()
    pygame.display.set_caption("Viborita Game")
    pantalla = pygame.display.set_mode((ancho,altura))

    corriendo = True

    while corriendo:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            x -= velocidad

        if teclas[pygame.K_RIGHT]:
            x += velocidad
        
        if teclas[pygame.K_UP]:
            y -= velocidad

        if teclas[pygame.K_DOWN]:
            y += velocidad


        pantalla.fill((30,0,128))
        pygame.draw.rect(pantalla, (0,200,10),(x,y,40,60))
        pygame.display.update()

main()

