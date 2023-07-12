from snake_game_utils import *

main_surface = make_screen()


snake_head = make_turtle("square", "blue")

snake_food = make_turtle("circle", "red")
change_food_position(snake_food)

running = True
while running:
    main_surface.update()
