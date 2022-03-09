import sys
import pygame


class Game:
    def __init__(self): 
        pygame.init()
        self.size = self.width, self.height = 320 * 2, 240 * 2
        self.speed = [1, 1]
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.ball, self.ballrect = self.load_image('sq.png')

    @staticmethod
    def load_image(image_name):
        img = pygame.image.load(image_name)
        pos = img.get_rect()
        return (img , pos)
        

    def move_ball(self):
        ballrect = self.ballrect.move(self.speed)
        if ballrect.left < 0 or ballrect.right > self.width:
            self.speed[0] = -self.speed[0]
        if ballrect.top < 0 or ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]
        self.ballrect = ballrect

    def draw(self):
        self.screen.fill(self.black)
        MyImg = Game.load_image('sq.png')
        self.screen.blit(MyImg[0] ,(MyImg[1][0] , MyImg[1][1]))
        pygame.display.update()


    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
