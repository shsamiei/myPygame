import pygame 

pygame.init()
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("My game ! ")

red = (255,0,0)
blue = (0,0,255)

turn = 0 


while True :
    pygame.event.pump()

    if turn == 0 : 
        screen.fill(red)
    else : 
        screen.fill(blue)

    turn = 1 -  turn 
    pygame.display.update()
    pygame.time.delay(200)


    


