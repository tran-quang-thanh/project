import pygame
from pygame.locals import *
import cv2
import numpy as np
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 255)
MAGENTA = (255, 0, 144)
display_surf = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
# display_surf = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dance")
window_width, window_height = pygame.display.get_surface().get_size()
fps = 30
fps_clock = pygame.time.Clock()

#  load images
upLeft = pygame.image.load("E:\\C4T\\Dance\\Pictures\\UpLeft.png")
upRight = pygame.image.load("E:\\C4T\\Dance\\Pictures\\UpRight.png")
downLeft = pygame.image.load("E:\\C4T\\Dance\\Pictures\\DownLeft.png")
downRight = pygame.image.load("E:\\C4T\\Dance\\Pictures\\DownRight.png")

upLeftActive = pygame.image.load("E:\\C4T\\Dance\\Pictures\\UpLeftActive.png")
upRightActive = pygame.image.load("E:\\C4T\\Dance\\Pictures\\UpRightActive.png")
downLeftActive = pygame.image.load("E:\\C4T\\Dance\\Pictures\\DownLeftActive.png")
downRightActive = pygame.image.load("E:\\C4T\\Dance\\Pictures\\DownRightActive.png")

center = pygame.image.load("E:\\C4T\\Dance\\Pictures\\Center.png")
glow = pygame.image.load("E:\\C4T\\Dance\\Pictures\\Glow.png")

#  load music
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.music.load("E:\\C4T\\Dance\\Music\\Lucky Strike.mp3")
pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(1)

#  starting positions

posUpLeft = (window_height / 2 - 74, window_height / 2 - 74)
posUpRight = (window_width - (window_height/2 -10), window_height / 2 - 74)
posDownLeft = (window_height/ 2 - 74, window_height / 2 + 10)
posDownRight = (window_width - (window_height/ 2 -10), window_height / 2 + 10)

#  button positions

buttonUpLeft = (10, 10)
buttonUpRight = (window_width - 74, 10)
buttonDownLeft = (10, window_height - 74)
buttonDownRight = (window_width - 74, window_height - 74)


class Point:

    def __init__(self, img, dir, start_pos, speed):
        self.points = []
        self.image = img
        self.direction = dir
        self.start_pos = start_pos
        self.speed = speed
        # self.points.append(list(self.start_pos))
        self.spawnTime = 0

    def move(self):
        # move
        for p in self.points:
            if self.direction == 1:  # upLeft
                if p[0] <= -64 and p[1] <= -64:
                    self.points.remove([p[0], p[1]])
                else:
                    p[0] -= self.speed
                    p[1] -= self.speed
            elif self.direction == 2:  # upRight
                if p[0] >= window_width and p[1] <= -64:
                    self.points.remove([p[0], p[1]])
                else:
                    p[0] += self.speed
                    p[1] -= self.speed
            elif self.direction == 3:  # downLeft
                if p[0] <= - 64 and p[1] >= window_height:
                    self.points.remove([p[0], p[1]])
                else:
                    p[0] -= self.speed
                    p[1] += self.speed
            elif self.direction == 4:  # downRight
                if p[0] >= window_width and p[1] >= window_height:
                    self.points.remove([p[0], p[1]])
                else:
                    p[0] += self.speed
                    p[1] += self.speed

        # draw
        for p in self.points:
            display_surf.blit(self.image, (p[0], p[1]))

    def add(self):
        self.points.append(list(self.start_pos))

    def spawn(self):
        self.spawnTime += 1

def distance(a, b, c, d):
    return math.sqrt((a-c)**2+(b-d)**2)

class Game:
    def __init__(self, speed=5):
        self.speed = speed
        point_speed = self.speed
        # points
        self.upLeft = Point(upLeft, 1, posUpLeft, point_speed)
        self.upRight = Point(upRight, 2, posUpRight, point_speed)
        self.downLeft = Point(downLeft, 3, posDownLeft, point_speed)
        self.downRight = Point(downRight, 4, posDownRight, point_speed)

    def update(self):
        # t = 35/89*distance(posUpLeft[0], posUpLeft[1], buttonUpLeft[0], buttonUpLeft[1])//self.speed
        # print(t)
        # t = 33.5
        if self.upLeft.spawnTime == 0:
            pygame.mixer.music.play(1)
        # if self.upLeft.spawnTime == 0:
        #     self.upLeft.add()
        # if self.upRight.spawnTime == 36:
        #     self.upRight.add()
        # if self.upLeft.spawnTime == 76:
        #     self.upLeft.add()
        # if self.upRight.spawnTime == 115:
        #     self.upRight.add()
        # if self.downRight.spawnTime == 142:  #moti
        #     self.downRight.add()
        # if self.upLeft.spawnTime == 180 and self.downRight.spawnTime == 180:
        #     self.upLeft.add()
        #     self.downRight.add()
        # if self.upRight.spawnTime == 195 and self.downLeft.spawnTime == 195:
        #     self.upRight.add()
        #     self.downLeft.add()
        # if self.downRight.spawnTime == 225 and self.downLeft.spawnTime == 225:
        #     self.downLeft.add()
        #     self.downRight.add()
        # if self.upRight.spawnTime == 235:  #yes
        #     self.upRight.add()
        # if self.upRight.spawnTime == 260:  #yes
        #     self.upRight.add()

        # if self.downLeft.spawnTime == 315:  #insti
        #     self.downLeft.add()
        # if self.upRight.spawnTime == 355 and self.downLeft.spawnTime == 355:
        #     self.upRight.add()
        #     self.downLeft.add()
        # if self.upLeft.spawnTime == 383 and self.downRight.spawnTime == 383:
        #     self.upLeft.add()
        #     self.downRight.add()
        # if self.downRight.spawnTime == 403 and self.downLeft.spawnTime == 403:
        #     self.downLeft.add()
        #     self.downRight.add()
        # if self.upLeft.spawnTime == 420:  #that's
        #     self.upLeft.add()
        # if self.upLeft.spawnTime == 447:  #that's
        #     self.upLeft.add()
        #
        # if self.downLeft.spawnTime == 474:
        #     self.downLeft.add()
        # if self.upLeft.spawnTime == 520:
        #     self.upLeft.add()
        # if self.upRight.spawnTime == 557:
        #     self.upRight.add()
        # if self.downRight.spawnTime == 594:
        #     self.downRight.add()
        # if self.downRight.spawnTime == 634:
        #     self.downRight.add()
        # if self.upRight.spawnTime == 674:
        #     self.upRight.add()
        # if self.upLeft.spawnTime == 713:
        #     self.upLeft.add()
        if self.downLeft.spawnTime == 752:
            self.downLeft.add()
        if self.downRight.spawnTime == 767 and self.downLeft.spawnTime == 767:
            self.downLeft.add()
            self.downRight.add()
        if self.downRight.spawnTime == 805 and self.downLeft.spawnTime == 805:
            self.downLeft.add()
            self.downRight.add()
        # if self.upRight.spawnTime == 837 and self.upLeft.spawnTime == 837:
        #     self.upLeft.add()
        #     self.upRight.add()
        # if self.upRight.spawnTime == 872 and self.upLeft.spawnTime == 872:
        #     self.upLeft.add()
        #     self.upRight.add()
        # if self.downRight.spawnTime == 907 and self.downLeft.spawnTime == 907:
        #     self.downLeft.add()
        #     self.downRight.add()
        # if self.downRight.spawnTime == 942 and self.downLeft.spawnTime == 942:
        #     self.downLeft.add()
        #     self.downRight.add()
        # if self.upRight.spawnTime == 977:
        #     self.upRight.add()
        # if self.upRight.spawnTime == 1012:
        #     self.upRight.add()
        #
        # if self.upRight.spawnTime == 1047 and self.upLeft.spawnTime == 1047:
        #     self.upRight.add()
        #     self.upLeft.add()
        # if self.downRight.spawnTime == 1082 and self.downLeft.spawnTime == 1082:
        #     self.downLeft.add()
        #     self.downRight.add()
        # if self.downLeft.spawnTime == 1117:
        #     self.downLeft.add()
        # if self.upLeft.spawnTime == 1152:
        #     self.upLeft.add()
        # if self.upRight.spawnTime == 1187:
        #     self.upRight.add()
        # if self.downRight.spawnTime == 1222:
        #     self.downRight.add()
        # if self.downRight.spawnTime == 1257 and self.downLeft.spawnTime == 1257:
        #     self.downLeft.add()
        #     self.downRight.add()
        # if self.upRight.spawnTime == 1292 and self.upLeft.spawnTime == 1292:
        #     self.upRight.add()
        #     self.upLeft.add()
        # if self.downRight.spawnTime == 1327:
        #     self.downRight.add()
        # if self.upRight.spawnTime == 1362:
        #     self.upRight.add()
        # if self.upLeft.spawnTime == 1397:
        #     self.upLeft.add()
        # if self.downLeft.spawnTime == 1432:
        #     self.downLeft.add()
        #
        # if self.upLeft.spawnTime == 1467:
        #     self.upLeft.add()
        # if self.upLeft.spawnTime == 1502:
        #     self.upLeft.add()
        # if self.upRight.spawnTime == 1537:
        #     self.upRight.add()
        # if self.upRight.spawnTime == 1572:
        #     self.upRight.add()
        # if self.downRight.spawnTime == 1607:
        #     self.downRight.add()
        # if self.downRight.spawnTime == 1642:
        #     self.downRight.add()
        # if self.upLeft.spawnTime == 1677:
        #     self.upLeft.add()
        # if self.upLeft.spawnTime == 1712:
        #     self.upLeft.add()

        self.upLeft.spawn()
        self.upLeft.move()
        self.upRight.spawn()
        self.upRight.move()
        self.downLeft.spawn()
        self.downLeft.move()
        self.downRight.spawn()
        self.downRight.move()


def Draw_Elements():
    display_surf.blit(upLeft, buttonUpLeft)
    display_surf.blit(upRight, buttonUpRight)
    display_surf.blit(downLeft, buttonDownLeft)
    display_surf.blit(downRight, buttonDownRight)
    display_surf.blit(center, posUpLeft)  # upLeft
    display_surf.blit(center, posUpRight)  # upRight
    display_surf.blit(center, posDownLeft)  # downLeft
    display_surf.blit(center, posDownRight)  # downRight


def main():
    pygame.init()
    game = Game()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (window_width, window_height), cv2.INTER_CUBIC)

        #  connect webcam

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        display_surf.blit(frame, (0, 0))

        Draw_Elements()
        game.update()
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()