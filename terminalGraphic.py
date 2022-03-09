
import pygame

pygame.init()

screen = pygame.display.set_mode((300 , 300))


white = (255, 255, 255)
your_color = (0,0,0)
yourPen_size = 1
list_of_points = []


screen.fill(white)

while True : 
    new_order = input().split()

    if new_order[0] == "draw" :

        if new_order[1] == "line": 
            pygame.draw.line(screen , your_color , (int(new_order[2]) , int(new_order[3])), (int(new_order[4]) , int(new_order[5])) ,yourPen_size)

        if new_order[1] == "circle" :
            pygame.draw.circle(screen , your_color , (int(new_order[2]), int(new_order[3])) , int(new_order[4]), yourPen_size)

        if new_order[1] == "polygon" :
            number_of_points = len(new_order) - 2 
            for i in range(number_of_points - 3):
                  my_tuple = (int(new_order[i+2]) , int(new_order[i+3]))
                  list_of_points.append(my_tuple)
            pygame.draw.polygon(screen ,  your_color , list_of_points ,yourPen_size )
            


    
    if new_order[0] == "change" :

        if new_order[1] == "size" :
            yourPen_size = int(new_order[2])      

        if new_order[1] == "color" :
            your_color = (int(new_order[2]) ,int(new_order[3]) ,int(new_order[4]) )


    if new_order[0] == "end":
        pygame.image.save(screen, 'draw.png')
        break
    







pygame.display.update()
while True :
    pygame.event.pump()


