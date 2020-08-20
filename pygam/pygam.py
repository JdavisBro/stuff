import pygame,os,sys,datetime,time

pygame.init()

size = width, height = 1600, 900

black = 0, 0, 255

screen = pygame.display.set_mode(size,pygame.RESIZABLE)

image = pygame.image.load("mario.png")
image = pygame.transform.scale(image, (200,200))

imagerect = image.get_rect()
imagerect = imagerect.move(20,0)

ground = pygame.Surface((width,100))
ground.fill((0,255,0))

groundrect = ground.get_rect()
groundrect = groundrect.move(0,800)

pygame.display.set_caption("it's a me mario")
pygame.display.set_icon(image)

start = datetime.datetime.now()
frames = 0
previousFrames = 0 
secondFrames = 0

font = pygame.font.SysFont("monospace", 20)
fps = font.render(f"{frames} fps", True, [0, 0, 0], [255, 255, 255])
second = datetime.datetime.now() + datetime.timedelta(seconds=1)

seconds = 1
gravity = True
pressed = []

currentFrameTime = 0 


class player():
    direction = 0 # 0 right 1 left
    speed = [0, 0]

cap = 2

def bind(val,minv,maxv):
    val += 0.49
    val = round(val)
    if val > maxv:
        return maxv
    elif val < minv:
        return minv
    return val

def frame():
    global imagerect, size, frames, size, gravity, width, height, screen, pressed, image, player, currentFrameTime, previousFrames, secondFrames, second
    frameTime = datetime.datetime.now() + datetime.timedelta(milliseconds=(1000/cap))
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
                player.speed = [0,0]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
            pressed.append(pygame.key.name(event.key))
        elif event.type == pygame.KEYUP:
            if pygame.key.name(event.key) in pressed:
                pressed.remove(pygame.key.name(event.key))

    imagerect = imagerect.move(0,1)

    if imagerect.colliderect(groundrect):
        player.speed[1] = 0
        while imagerect.colliderect(groundrect):
            imagerect = imagerect.move(0,-1)
        imagerect = imagerect.move(0,1)
    else:
        player.speed[1] += 0.5

    if pygame.key.get_pressed()[pygame.K_d] == 1:
        player.speed[0] += 1
        if player.direction != 0 and player.speed[0] > 0:
            player.direction = 0
            image = pygame.transform.flip(image,True,False)
    elif pygame.key.get_pressed()[pygame.K_a] == 1:
        player.speed[0] -= 1
        if player.direction != 1 and player.speed[0] < 0:
            player.direction = 1
            image = pygame.transform.flip(image,True,False)
    else:
        player.speed[0] += 1 if player.speed[0] < 0 else 0
        player.speed[0] -= 1 if player.speed[0] > 0 else 0

    imagerect = imagerect.move(0,-1)

    player.speed[0] = bind(player.speed[0],-50,50)
    player.speed[1] = bind(player.speed[1],-50,50)

    imagerect = imagerect.move(player.speed)

    if imagerect.top > size[1]:
        imagerect.bottom = 0

    if imagerect.bottom < 0:
        imagerect.top = size[1]

    if imagerect.left > size[0]:
        imagerect.right = 0

    if imagerect.right < 0:
        imagerect.left = size[0]

    frames += 1

    seconds = (datetime.datetime.now() - start).seconds + round((datetime.datetime.now() - start).microseconds / 1000000,2)

    if seconds == 0.0:
        seconds = 1

    secondFrames += 1

    if datetime.datetime.now() >= second:
        second = datetime.datetime.now() + datetime.timedelta(seconds=1)
        previousFrames = secondFrames
        secondFrames = 0

    fps = font.render(f"fps {previousFrames} af {frames/seconds:.2f} ({frames}/{seconds:.2f}) s ({player.speed[0]:.2f} x {player.speed[1]:.2f} y) p ({imagerect.x} x {imagerect.y} y) g {'y' if gravity else 'n'} k {pressed}", True, [0, 0, 0], [255, 255, 255])

    screen.fill(black)
    screen.blit(ground, groundrect)
    screen.blit(image, imagerect)
    screen.blit(fps,fps.get_rect())

    pygame.display.flip()

    if datetime.datetime.now() < frameTime:
        currentFrameTime = (frameTime - datetime.datetime.now()).microseconds/1000000
        time.sleep(currentFrameTime)

while 1:
    frame()