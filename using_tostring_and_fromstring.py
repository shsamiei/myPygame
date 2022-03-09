import pygame
img = pygame.image.load('out.png')
size = img.get_rect().size
pic_string = pygame.image.tostring(img ,'RGB')
# print(type(pic_string))
# print(pic_string)


img2 = pygame.image.fromstring(pic_string, size , 'RGB')
# print(type(img2))
# print(img2)
pygame.image.save(img2 , 'output.png')