import pygame, time
pygame.init()

screen_width = 1000
screen_height = 1000
first = True
skip = False
index = 0
currentframe = 0
printer = "false"
letters = []
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

title_text = pygame.image.load("assets/title.png")

class snake(object):
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (490, 500, 50, 50))

done_printing = False
class letter_object(object):
    def __init__(self, type, pos, index):
        self.type = type
        self.pos = pos
        self.index = index
    def print(self):
        if self.index >= 69:
            win.blit(pygame.image.load("assets/letters/low/" + self.type + ".png"), (self.pos, 900))
        elif self.index >= 46:
            win.blit(pygame.image.load("assets/letters/low/" + self.type + ".png"), (self.pos, 800))
        elif self.index >= 23:
            win.blit(pygame.image.load("assets/letters/low/" + self.type + ".png"), (self.pos, 700))
        else:
            win.blit(pygame.image.load("assets/letters/low/" + self.type + ".png"), (self.pos, 600))



def lettergen(text, speed):
    global done_printing, first, index, pos, currentframe, skip
    if first:
        if text.__len__() > 24:
            pos = 40
        else:
            pos = 500 - str(text).__len__() * 20 + 20
        first = False
    if not done_printing:
        if skip:
            if text.__len__() > 24:
                pos = 40
            else:
                pos = 500 - str(text).__len__() * 20 + 20
            for letter in str(text):
                if pos >= 960:
                    pos = 40
                if str(letter) in "abcdefghijklmnopqrstuvwxyz":
                    letters.append(letter_object(str(letter), pos, index))
                if str(letter) == "^":
                    pos = 40
                    if index < 23:
                        index = 23
                    elif index < 46:
                        index = 46
                    elif index < 69:
                        index = 69
                else:
                    pos += 40
                index += 1

            index = 0
            done_printing = True
            skip = False
            first = True
        elif currentframe < speed:
           currentframe += 1
        elif currentframe == speed:
            currentframe = 0
            if pos >= 960:
                pos = 40
            letter = str.lower(text[index])
            if letter in "abcdefghijklmnopqrstuvwxyz":
                letters.append(letter_object(letter, pos, index))
            if str(letter) == "^":
                pos = 40
                if index < 23:
                    index = 23
                elif index < 46:
                    index = 46
                elif index < 69:
                    index = 69
            else:
                pos += 40
            index += 1
            if index == str(text).__len__():
                index = 0
                done_printing = True
                first = True

def clear_letters():
    global letters, printer
    letters = []
    printer = "false"

head = snake(500, 500, 1)

def draw(win):
    global title_pulse
    win.fill((255, 255, 255))
    head.draw(win)
    for object in letters:
        object.print()
    if printer != "false":
        global pos
        if first:
            pos = 500 - str(printer).__len__() * 20
        lettergen(printer, 2)
    pygame.display.update()

clock = pygame.time.Clock()
titlescreen = True
title_pulse = 0
game_running = True
while game_running:
    clock.tick(30)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            print("Program exited by user")
            game_running = False

    if keys[pygame.K_LEFT]:
        titlescreen = False
        if printer == "false":
            printer = "gooooood morning gamers"
            done_printing = False
    if keys[pygame.K_RIGHT]:
        titlescreen = False
        if printer == "false":
            printer = "but nobody came"
            done_printing = False

    if keys[pygame.K_UP]:
        titlescreen = False
        if printer == "false":
            printer = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            done_printing = False
    if keys[pygame.K_DOWN]:
        titlescreen = False
        if not done_printing:
            skip = True
        else:
            clear_letters()
            skip = False




    draw(win)