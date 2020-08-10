import pygame,os,sys,datetime

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
start = datetime.datetime.now()
time = datetime.datetime.now() + datetime.timedelta(seconds=1)
frames = 0
previousFrames = 0 
font = pygame.font.SysFont("monospace", 20)
fps = font.render(f"{frames} fps", True, [0, 0, 0], [255, 255, 255])
seconds = 1
gravity = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size,pygame.RESIZABLE)
            size = width, height = event.size
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                if gravity:
                    gravity = False
                else:
                    gravity = True
            elif event.key == pygame.K_r:
                acceleration = [0,0]
                speed = [0,0]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()

    imagerect = imagerect.move(0,1)

    if imagerect.colliderect(groundrect):
        if gravity:
            speed[1] = 0
    else:
        if gravity:
            speed[1] += 0.25
    if speed[1] > 2:
        speed[1] = 2
    if speed[1] < -2:
        speed[1] = -2

    if pygame.key.get_pressed()[pygame.K_a] == 1:
        speed[0] -= 0.25 if speed[0] >= -2 else 0
        if speed[0] < 0 and (direction == 1 and imagerect.colliderect(groundrect)):
            direction = 0
            image = pygame.transform.flip(image,True,False)
    else:
        if gravity:
            speed[0] += 0.25 if speed[0] < 0 else 0

    if pygame.key.get_pressed()[pygame.K_d] == 1:
        speed[0] += 0.25 if speed[0] <= 2 else 0
        if speed[0] > 0 and (direction == 0 and imagerect.colliderect(groundrect)):
            direction = 1
            image = pygame.transform.flip(image,True,False)
    else:
        if gravity:
            speed[0] -= 0.25 if speed[0] > 0 else 0

    if pygame.key.get_pressed()[pygame.K_w]:
        if (not jumped and imagerect.colliderect(groundrect) == 1) or not gravity:
            acceleration[1] = -1
            jumped = True
    else:
        jumped = False

    if pygame.key.get_pressed()[pygame.K_s] == 1:
        acceleration[1] = 1
    else:
        if gravity:
            while imagerect.colliderect(groundrect):
                imagerect = imagerect.move(0,-1)

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

    if imagerect.top > size[1]:
        imagerect.bottom = 0

    if imagerect.bottom < 0:
        imagerect.top = size[1]

    if imagerect.left > size[0]:
        imagerect.right = 0

    if imagerect.right < 0:
        imagerect.left = size[0]

    frames += 1

    if time < datetime.datetime.now():
        time = datetime.datetime.now() + datetime.timedelta(seconds=1)

    seconds = (datetime.datetime.now() - start).seconds + round((datetime.datetime.now() - start).microseconds / 1000000,2)

    if seconds == 0.0:
        seconds = 1

    fps = font.render(f"{frames/seconds:.2f} fps - speed ({speed[0]:.2f} x {speed[1]:.2f} y) - {frames} frames - {seconds:.2f} seconds - accel ({acceleration[0]:.2f} x {acceleration[1]:.2f} y) - coord ({imagerect.x} x {imagerect.y} y) - gravity {gravity}", True, [0, 0, 0], [255, 255, 255])

    screen.fill(black)
    screen.blit(ground, groundrect)
    screen.blit(image, imagerect)
    screen.blit(fps,fps.get_rect())
    pygame.display.flip()