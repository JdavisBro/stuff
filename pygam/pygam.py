import pygame,os,sys

pygame.init()

size = width, height = 1600, 900
speed = [0, 0]
black = 0, 0, 255

screen = pygame.display.set_mode(size,pygame.RESIZABLE)

image = pygame.image.load("mario.png")
image = pygame.transform.scale(image, (200,200))
imagerect = image.get_rect()
imagerect = imagerect.move(20,0)
ground = pygame.Surface((width,400))
ground.fill((0,255,0))
groundrect = ground.get_rect()
groundrect = groundrect.move(0,500)
pygame.display.set_caption("it's a me mario")
pygame.display.set_icon(image)
direction = 1
acceleration = [0,0]
jumped = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size,pygame.RESIZABLE)
            size = width, height = event.size
    imagerect = imagerect.move(0,1)
    if imagerect.colliderect(groundrect):
        speed[1] = 0
    else:
        speed[1] += 1.5
    if speed[1] > 50:
        speed[1] = 50

    if pygame.key.get_pressed()[pygame.K_a] == 1:
        speed[0] -= 0.25 if speed[0] >= -50 else 0
        if speed[0] < 0 and direction == 1:
            direction = 0
            image = pygame.transform.flip(image,True,False)
    else:
        speed[0] += 0.25 if speed[0] < 0 else 0

    if pygame.key.get_pressed()[pygame.K_d] == 1:
        speed[0] += 0.25 if speed[0] <= 50 else 0
        if speed[0] > 0 and direction == 0:
            direction = 1
            image = pygame.transform.flip(image,True,False)
    else:
        speed[0] -= 0.25 if speed[0] > 0 else 0

    if pygame.key.get_pressed()[pygame.K_w]:
        if not jumped and imagerect.colliderect(groundrect) == 1:
            acceleration[1] = -7
            jumped = True
    else:
        jumped = False

    if acceleration[0] != 0 or acceleration[1] != 0:
        speed[0] += acceleration[0]
        speed[1] += acceleration[1]
        if acceleration[0] > 0:
            acceleration[0] -= 1
        if acceleration[0] < 0:
            acceleration[0] += 1
        if acceleration[1] > 0:
            acceleration[1] -= 1
        if acceleration[1] < 0:
            acceleration[1] += 1

    imagerect = imagerect.move(0,-1)

    imagerect = imagerect.move(speed)

    while imagerect.colliderect(groundrect):
        imagerect = imagerect.move(0,-1)

    if imagerect.top > size[1]:
        imagerect.bottom = 0

    if imagerect.left > size[0]:
        imagerect.right = 0

    if imagerect.right < 0:
        imagerect.left = size[0]

    screen.fill(black)
    screen.blit(ground, groundrect)
    screen.blit(image, imagerect)
    pygame.display.flip()
