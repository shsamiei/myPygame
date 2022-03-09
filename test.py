





#pygame.draw.polygon(screen , red , [(700, 500), (600, 500), (550, 450), (650, 440)] ,25 )

order = input().split()
number_of_points = len(order) - 2 
print(number_of_points)
list_of_points = []
for i in range(number_of_points - 3):
    my_tuple = (order[i+2] , order[i+3])
    list_of_points.append(my_tuple)

print(list_of_points)


