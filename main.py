import pygame

window = pygame.display.set_mode ((400, 400))
pygame.display.set_caption('MasyaCat')

screen = pygame.Surface((400, 400))

run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill((170, 180, 170))
    window.blit(screen, (0, 0))
    pygame.display.flip()
