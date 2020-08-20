import datetime
import sys

import pygame

pygame.init()

class screen(): 
    size = height, width = 1600,900
    screen = pygame.display.set_mode(size,pygame.RESIZABLE)

class variables():
    startTime = datetime.datetime.now()
    totalFrames = 0
    secondFrames = 0
    lastSecondFrames = 0
    totalSeconds = 0
    keysPressed = []

class objects():

    class player():
        direction = 0 # 0 right 1 left
        speed = [0, 0]
        image = pygame.image.load("mario.png")
        image = pygame.transform.scale(image, (200,200))
        rect = image.get_rect()
        rect = rect.move(20,0)

    font = pygame.font.SysFont("monospace", 20)

    debugDisplay = None

def bind(val,minv,maxv):
    val += 0.49
    val = round(val)
    if val > maxv:
        return maxv
    elif val < minv:
        return minv
    return val

def event(e):
    if e.type == pygame.QUIT: sys.exit()

    elif e.type == pygame.VIDEORESIZE:
        screen.screen = pygame.display.set_mode(e.size,pygame.RESIZABLE)
        screen.size = screen.width, screen.height = e.size

    elif e.type == pygame.KEYDOWN:
        variables.keysPressed.append(pygame.key.name(e.key))

    elif e.type == pygame.KEYUP:
        variables.keysPressed.remove(pygame.key.name(e.key))


def frame():
    global objects, variables, screen

    frameStart = datetime.datetime.now()

    for e in pygame.event.get():
        event(e)

    objects.player.speed[1] += 1

    objects.player.speed[0] = bind(objects.player.speed[0],-20,20)
    objects.player.speed[1] = bind(objects.player.speed[1],-20,20)

    objects.player.rect = objects.player.rect.move(objects.player.speed)

    if objects.player.rect.top > screen.size[1]:
        objects.player.rect.bottom -= screen.size[1]
    if objects.player.rect.bottom < 0:
        objects.player.rect.top += screen.size[1]
    if objects.player.rect.left > screen.size[0]:
        objects.player.rect.right -= screen.size[0]
    if objects.player.rect.right < 0:
        objects.player.rect.left += screen.size[0]

    variables.totalFrames += 1
    variables.secondFrames += 1

    variables.totalSeconds += (datetime.datetime.now() - frameStart).seconds + ((datetime.datetime.now() - frameStart).microseconds / 1000000)

    print((datetime.datetime.now() - frameStart).seconds,(datetime.datetime.now() - frameStart).microseconds,(datetime.datetime.now() - frameStart).seconds + (datetime.datetime.now() - frameStart).microseconds/1000000)

    objects.debugDisplay = objects.font.render(f"fps {variables.lastSecondFrames} af {(variables.totalFrames/variables.totalSeconds) if variables.totalSeconds != 0 else 1:.2f} ({variables.totalFrames}/{variables.totalSeconds:.2f}) s ({objects.player.speed[0]:.2f} x {objects.player.speed[1]:.2f} y) p ({objects.player.rect.x} x {objects.player.rect.y} y) k {variables.keysPressed}", True, [0, 0, 0], [255, 255, 255])
    screen.screen.fill((0,0,255))
    screen.screen.blit(objects.player.image, objects.player.rect)
    screen.screen.blit(objects.debugDisplay,objects.debugDisplay.get_rect())

    pygame.display.flip()

while 1:
    frame()
