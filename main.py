import pygame
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('chess')
myIcon = pygame.image.load("C:\\Users\\annro\Downloads\\ferz2.bmp")
pygame.display.set_icon(myIcon)

BROWN = (90, 50, 20)
GREEN = (0, 255, 0)
FPS = 30
clock = pygame.time.Clock()






W = 600
H = 400
x = W//4
y = H //2
speed = 10

def change_pos(speed):
    global x, y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x -= speed
        if event.key == pygame.K_RIGHT:
            x += speed
        if event.key == pygame.K_DOWN:
            y += speed
        if event.key == pygame.K_UP:
            y -= speed

right = left = False
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key  == pygame.K_RIGHT:
                right = True
        elif event.type == pygame.KEYUP:
            if event.key in pygame.K_LEFT or  pygame.K_RIGHT:
                right = left = False
    if left:
        x -=speed
    if right:
        x +=speed



    screen.fill(BROWN)
    pygame.draw.rect(screen, GREEN, (x, y, 10, 20))
    pygame.display.update()
    clock.tick(FPS)






