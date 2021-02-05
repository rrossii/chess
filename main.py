import pygame
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('chess')
myIcon = pygame.image.load("C:\\Users\\annro\Downloads\\ferz2.bmp")
BROWN = (90, 50, 20)
FPS = 30
clock = pygame.time.Clock()

pygame.display.set_icon(myIcon)
screen.fill(BROWN)

pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 100))
pygame.display.flip()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


