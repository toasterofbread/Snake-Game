import pygame, time
pygame.init()

screen_width = 1000
screen_height = 1000

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

title_text = pygame.image.load("assets/title.png")

class snake(object):
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
    def draw(self, win):
        if direction == "up":
            self.y -= snake_velocity
        elif direction == "down":
            self.y += snake_velocity
        elif direction == "right":
            self.x += snake_velocity
        elif direction == "left":
            self.x -= snake_velocity
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, 25, 25))

def death_check():
    global dead, titlescreen, direction
    if segments[0].x > 950 or segments[0].x < 0 or segments[0].y > 950 or segments[0].y < 0:
        titlescreen = True
        direction = ""
        pygame.draw.rect(win, (0, 0, 0), (0, 0, 1000, 1000))
        pygame.draw.rect(win, (255, 0, 0), (5, 5, 990, 990))
        if segments[0].x < 0:
            segments[0].x = 0
        if segments[0].y < 0:
            segments[0].y = 0
        pygame.draw.rect(win, (0, 0, 0), (segments[0].x, segments[0].y, 25, 25))
        pygame.display.update()
        segments[0].x = 500
        segments[0].y = 500
        time.sleep(0.5)


def draw(win):
    global title_pulse, dead
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 1000, 1000))
    pygame.draw.rect(win, (255, 255, 255), (5, 5, 990, 990))
    death_check()
    if not dead:
        segments[0].draw(win)
    if titlescreen:
        if title_pulse < 30:
            win.blit(title_text, (100, 600))
            title_pulse += 1
        elif title_pulse < 45:
            title_pulse += 1
        else:
            title_pulse = 0
    pygame.display.update()

titlescreen = True
title_pulse = 0

direction = ""
snake_velocity = 25
dead = False

segments = [snake(475, 475, 1)]

game_running = True
clock = pygame.time.Clock()

while game_running:
    clock.tick(20)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] or (keys[308] and keys[pygame.K_F4]):
            print("Program exited by user")
            game_running = False
    if game_running:
        if keys[pygame.K_LEFT]:
            titlescreen = False
            title_pulse = 0
            direction = "left"
        if keys[pygame.K_RIGHT]:
            titlescreen = False
            title_pulse = 0
            direction = "right"
        if keys[pygame.K_UP]:
            titlescreen = False
            title_pulse = 0
            direction = "up"
        if keys[pygame.K_DOWN]:
            titlescreen = False
            title_pulse = 0
            direction = "down"
        if keys[pygame.K_a]:
            titlescreen = False
            title_pulse = 0
        draw(win)