#   A random clicking game made to learn more about python
#   Made by: Zeoffin
#   v 1.0

import pygame
import random
import time
import threading

pygame.init()

display_x = 800
display_y = 600

display = pygame.display.set_mode((display_x, display_y))

pygame.display.set_caption("Reactionery - The Game")

clock = pygame.time.Clock()

game_exit = False
game_over = False

time_left = 5
intro_time = 3

# Define colors
colors = []

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 100, 10)
yellow = (255, 255, 0)
blue_green = (0, 255, 170)
marroon = (115, 0, 0)
lime = (180, 255, 100)
pink = (255, 100, 180)
purple = (240, 0, 255)
gray = (127, 127, 127)
magenta = (255, 0, 230)
brown = (100, 40, 0)
forest_green = (0, 50, 0)
navy_blue = (0, 0, 100)
rust = (210, 150, 75)
dandilion_yellow = (255, 200, 0)
highlighter = (255, 255, 100)
sky_blue = (0, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (50, 50, 50)
tan = (230, 220, 170)
coffee_brown =(200, 190, 140)
moon_glow = (235, 245, 255)

colors.append(black)
colors.append(blue)
colors.append(green)
colors.append(red)
colors.append(orange)
colors.append(yellow)
colors.append(blue_green)
colors.append(marroon)
colors.append(lime)
colors.append(pink)
colors.append(purple)
colors.append(gray)
colors.append(magenta)
colors.append(brown)
colors.append(forest_green)
colors.append(navy_blue)
colors.append(rust)
colors.append(dandilion_yellow)
colors.append(highlighter)
colors.append(sky_blue)
colors.append(light_gray)
colors.append(dark_gray)
colors.append(tan)
colors.append(coffee_brown)
colors.append(moon_glow)


# Functions


def game_menu():

    menu = True
    screen_filled = False

    while menu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game()

        # display.fill(white)
        # message(310, 250, 50, "Reactionery", black)
        # message(355, 290, 30, "The Game", black)
        # time.sleep(3)
        #
        # pygame.display.update()

        display.fill(white)
        message(150, 240, 40, "Click on colored boxes. SPACE to restart", black)
        message(310, 290, 30, "You have {} seconds!".format(time_left), black)

        start_thread(intro_timer)

        while not screen_filled:

            pygame.display.update()

            if intro_time < 1:
                screen_filled = True
                menu = False


def intro_timer():

    global intro_time
    active = True

    while active:

        pixel_color = random.choice(colors)
        pixel_x = random.randrange(0, 800)
        pixel_y = random.randrange(0, 600)

        print(intro_time)
        intro_time -= 0.1
        draw_object(display, pixel_color, pixel_x, pixel_y, 10, 10)
        time.sleep(0.1)

        pygame.display.update()

        clock.tick(200)

        if intro_time < 1:
            active = False


def timer():

    global game_over
    global time_left

    while not game_over:

        # Clear old time
        draw_object(display, white, 696, 8, 60, 30)

        print(time_left)
        time_left -= 0.01
        time.sleep(0.01)

        if time_left < 0:
            game_over = True


def start_thread(method):

    timer_thread = threading.Thread(target=method)
    timer_thread.daemon = True  # Stop thread if exiting out of program
    timer_thread.start()


def draw_object(screen, color, object_x, object_y, object_width, object_height):

    pygame.draw.rect(screen, color, [object_x, object_y, object_width, object_height])


def message(width, height, font_size, msg, color):

    font = pygame.font.SysFont(None, font_size)

    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [width, height])

    pygame.display.update()


def exit_game():

    pygame.quit()
    quit()


def game_loop():

    global game_exit
    global game_over
    global time_left

    game_over = False

    # game_exit = False
    # game_over = False

    object_width_maximum = 400
    object_height_maximum = 400

    object_width_minimum = 250
    object_height_minimum = 250

    # Object
    coordinate_min_x = 30
    coordinate_max_x = 770

    coordinate_y_min = 30
    coordinate_y_max = 570

    object_x = random.randrange(coordinate_min_x, coordinate_max_x)
    object_y = random.randrange(coordinate_y_min, coordinate_y_max)

    object_width = random.randrange(object_width_minimum, object_width_maximum)
    object_height = random.randrange(object_height_minimum, object_height_maximum)

    start_thread(timer)

    time_left = 5

    score = 0

    added_time = 2

    object_color = random.choice(colors)

    display.fill(white)

    while not game_exit:

        # Losing
        while game_over:

            display.fill(white)

            message(190, (display_y / 2) - 50, 50, "Game over. Your score: {}".format(score), black)
            message(display_x / 3, (display_y / 2), 30, "Press SPACE to play again", black)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        game_exit = True
                        game_over = False

                    elif event.key == pygame.K_SPACE:
                        game_loop()

                elif event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        object_maximum_x = object_width + object_x
        object_maximum_y = object_height + object_y

        # Event handling
        for event in pygame.event.get():

            # Exit game
            if event.type == pygame.QUIT:
                game_exit = True

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_exit = True

                elif event.key == pygame.K_SPACE:
                    game_loop()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Clicked on object
                if (object_maximum_x >= mouse_x >= object_x) and (object_maximum_y >= mouse_y >= object_y):

                    # Decrease object size
                    if object_height_minimum > 40:

                        object_width_maximum -= 2
                        object_height_maximum -= 2
                        object_width_minimum -= 2
                        object_height_minimum -= 2

                    object_x = random.randrange(coordinate_min_x, coordinate_max_x)
                    object_y = random.randrange(coordinate_y_min, coordinate_y_max)

                    object_width = random.randrange(object_width_minimum, object_width_maximum)
                    object_height = random.randrange(object_height_minimum, object_height_maximum)

                    display.fill(white)

                    score += 1

                    added_time = added_time * 0.9

                    time_left += added_time

                    object_color = random.choice(colors)

                    if score % 20 == 0:
                        time_left += 5

                    elif score % 100 == 0:
                        time_left += 5

                    pygame.display.update()

                # Lost by clicking outside the box
                else:
                    game_over = True

        # Draw object
        draw_object(display, object_color, object_x, object_y, object_width, object_height)

        # Display time left & score
        # TODO: Kaut kā vajaga redraw visu laiku
        message(600, 10, 30, "Time left: {:.2f}".format(time_left), black)
        message(600, 40, 30, "Score: {}".format(score), black)

        pygame.display.update()

        clock.tick(500)

    exit_game()


game_menu()
game_loop()

