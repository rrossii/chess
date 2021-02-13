import pygame
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('chess')
myIcon = pygame.image.load("C:\\Users\\annro\Downloads\\ferz2.bmp")
pygame.display.set_icon(myIcon)

PURPLE = (153, 102, 204)
GREEN = (208, 240, 192)
FPS = 60
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


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

start = None


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(PURPLE)
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():

        pygame.draw.circle(screen, GREEN, pos, 5)

    pressed = pygame.mouse.get_pressed()

    if pressed[0]:

        if start is None:
            start = pos
        width = pos[0] - start[0]
        height = pos[1] - start[1]

        
        pygame.draw.rect(screen, GREEN, (start[0], start[1], width, height))
    else:
        start = None


    pygame.display.update()
    clock.tick(FPS)






