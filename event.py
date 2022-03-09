from asyncio import events
from cmath import pi
from curses.ascii import isblank
import pygame

pygame.init()
screen  = pygame.display.set_mode((800,600))

blue = (0 ,255, 255)
pink = (255 ,0, 255)

isBlue = True

screen.fill(blue)
pygame.display.update()

# Quit Event :

# while True : 
#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         if isBlue == True :
#             screen.fill(pink)
#             isBlue = False
#         else : 
#             screen.fill(blue)
#             isBlue = True
#         pygame.display.update()
#         print('QUIT EVENT ! ')


# Keydown Event :

# while True : 
#     event = pygame.event.wait()

#     if event.type == pygame.KEYDOWN:
#         if isBlue == True :
#             screen.fill(pink)
#             isBlue = False
#         else:
#             screen.fill(blue)
#             isBlue = True
#         pygame.display.update()

#         print("Keydown Event ! ")
#         print(f"Key Code is : {event.key}")
#         print(f"Key Unicode is : {event.unicode}")

#     if event.type == pygame.QUIT :
#         pygame.quit()
#         break

    

# keyUp Event : 

# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.KEYUP:
#         if isBlue is True:
#             screen.fill(pink)
#             isBlue = False
#         else:
#             screen.fill(blue)
#             isBlue = True
#         pygame.display.update()
#         print('Key Up Event!')
#         print(f"Key Code is : {event.key}")
#         print(f"Key Unicode is : {event.unicode}")

#     if event.type == pygame.QUIT:
#         pygame.quit()
#         break

# MouseButtonDown Event : 

# while True : 
#     event = pygame.event.wait()
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if isBlue == True : 
#             screen.fill(pink)
#             isBlue = False
#         else : 
#             screen.fill(blue)
#             isBlue = True
#         pygame.display.update()
#         print("mousebuttomDOwn Event ! ")
#         print(f"Key Position is : {event.pos}")
#         print(f"Key Button is : {event.button}")
#     if event.type == pygame.QUIT :
#         pygame.quit()
#         break

# MouseButtonUp Event : 

# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# blue = (0, 255, 255)
# pink = (255, 0, 255)
# is_blue = True
# screen.fill(blue)
# pygame.display.update()
# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.MOUSEBUTTONUP:
#         if is_blue is True:
#             screen.fill(pink)
#             is_blue = False
#         else:
#             screen.fill(blue)
#             is_blue = True
#         pygame.display.update()
#         print('Mouse Button Up Event!')
#         print(f"Key Position is : {event.pos}")
#         print(f"Key Button is : {event.button}")

#     if event.type == pygame.QUIT:
#         pygame.quit()
#         break

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
blue = (0, 255, 255)
pink = (255, 0, 255)
is_blue = True
screen.fill(blue)
pygame.display.update()
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEMOTION:
        if is_blue is True:
            screen.fill(pink)
            is_blue = False
        else:
            screen.fill(blue)
            is_blue = True
        pygame.display.update()
        print('Mouse Motion Event!')
        print(f"Key Position is : {event.pos}")
        print(f"Key Button is : {event.rel}")

    if event.type == pygame.QUIT:
        pygame.quit()
        break