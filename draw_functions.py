import pygame
from math import pi 

pygame.init()

screen = pygame.display.set_mode((800,600))


red = (255, 0, 0)

blue = (0, 0, 255)

green = (0, 255, 0)

gray = (128, 128, 128)

screen.fill(gray)

# How to draw line in pygame : 

pygame.draw.line(screen , green , (300,300) , (600 ,400))

# How to draw a circle in pygame :

pygame.draw.circle(screen , blue , (200 ,200) , 20)

# How to draw rect :

pygame.draw.rect(screen , blue , (400 ,400 , 30 , 80) , 10)

# How to draw ellipse : 

pygame.draw.ellipse(screen , red  , (450 , 450 , 100 , 50 ) , 40)

# How to draw polygan : 

pygame.draw.polygon(screen , red , [(700, 500), (600, 500), (550, 450), (650, 440)] ,25 )

# How to draw connected lines : 

# in this mode the first point and the last point is connected : 
pygame.draw.lines(screen , blue , True , [(700, 200), (600, 200), (550, 150), (650, 140)])

# in this mode the last pointe and the first point is not connected ! :
pygame.draw.lines(screen , blue , False , [(700, 350), (600, 350), (550, 300), (650, 290)])

# How to draw arc :
pygame.draw.rect(screen , red , (210, 75, 150, 125)  )
pygame.draw.arc(screen , green ,  (210, 75, 150, 125), 3*pi/2, 2*pi)


pygame.display.update()

while True :
    pygame.event.pump()
    

