import pygame

## first version  using load 


# img = pygame.image.load('sq.png')

# white = (255,255,255)
# screen = pygame.display.set_mode((640 , 480))
# screen.fill(white)

# x , y = 0 , 0

# while True : 
#     screen.fill(white)
#     screen.blit(img , (x,y))
#     x , y = x+1 , y+5
#     pygame.display.update()
#     pygame.time.delay(13)
#     pygame.event.pump()




# second version : 

dx , dy = map(int , input().split())
t = int(input())

img = pygame.image.load('sq.png')

white = (255, 255 , 255)
screen = pygame.display.set_mode((640 , 480))
screen.fill(white)

x , y = 0 , 0 

# for i in range(t) :
#     screen.fill(white)
#     screen.blit(img , (x,y))
#     x , y = x + dx , y + dy


# pygame.image.save(screen , 'out.png')

m = 0 
while True :
    screen.fill(white)
    screen.blit(img , (x,y))
    x , y = x + dx , y + dy
    m = m+1 
    pygame.display.update()
    pygame.time.delay(13)
    pygame.event.pump()
    if m == 100 :
        pygame.image.save(screen , 'out.png')
    







