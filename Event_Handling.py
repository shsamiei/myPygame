import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


# wait() method waits untill an event happen 

# while True:
#     event = pygame.event.wait()

#     if event.type == pygame.QUIT:
#         print('Quit')

#     if event.type == pygame.KEYDOWN:
#         print('Key Down')
#         print(event.key)
#         print(event.unicode)

#     if event.type == pygame.KEYUP:
#         print('Key Up')
#         print(event.key)

#     if event.type == pygame.MOUSEBUTTONDOWN:
#         print('Mouse Button Down')
#         print(event.pos)
#         print(event.button == pygame.BUTTON_RIGHT)
#         print(event.button == pygame.BUTTON_LEFT)

#     if event.type == pygame.MOUSEBUTTONUP:
#         print('Mouse Button Up')
#         print(event.pos)
#         print(event.button == pygame.BUTTON_RIGHT)
#         print(event.button == pygame.BUTTON_LEFT)

#     if event.type == pygame.MOUSEMOTION:
#         print('Mouse Motion')
#         print(event.pos)
#         print(event.rel)

# poll() method return the last event , if there is no event return NOEVENT

# events = []
# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         print('Quit')

#     if event.type == pygame.KEYDOWN:
#         print('Key Down')
#         print(event.key)
#         print(event.unicode)

#     if event.type == pygame.KEYUP:
#         print('Key Up')
#         print(event.key)

#     if event.type == pygame.MOUSEBUTTONDOWN:
#         print('Mouse Button Down')
#         print(event.pos)
#         print(event.button == pygame.BUTTON_RIGHT)
#         print(event.button == pygame.BUTTON_LEFT)

#     if event.type == pygame.MOUSEBUTTONUP:
#         print('Mouse Button Up')
#         print(event.pos)
#         print(event.button == pygame.BUTTON_RIGHT)
#         print(event.button == pygame.BUTTON_LEFT)

#     if event.type == pygame.MOUSEMOTION:
#         print('Mouse Motion')
#         print(event.pos)
#         print(event.rel)

#     event = pygame.event.poll()
#     if event.type is pygame.NOEVENT:
#        break
#     else:
#        events.append(event) 



# get() method in Event Handling : 


# while True:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             exit()
#     screen.fill((255, 255, 255))
#     pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
#     pygame.display.flip()


screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("test window")

red = (255, 0, 0)
blue = (0, 0, 255)

turn = 0
while True:
    pygame.event.pump()

    if turn == 0:
        screen.fill(red)
    else:
        screen.fill(blue)
    turn = 1 - turn
    pygame.display.update()
    pygame.time.delay(200)