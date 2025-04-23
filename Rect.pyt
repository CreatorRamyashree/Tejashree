import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
red = (255, 0, 200)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (20, 0, 200), pygame.Rect(60, 60, 80, 80))
    pygame.draw.circle(screen, red,(300, 300), 50)
    pygame.draw.circle(screen, red,(100, 100), 50, 3)
    pygame.display.update()
    pygame.display.flip()