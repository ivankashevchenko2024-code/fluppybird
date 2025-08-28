from random import randint
from pygame import *

init()
window_size = 1000, 680
window = display.set_mode(window_size)
clock = time.Clock()

player_rect = Rect(80, 200, 80, 80)

def generate_pipes(count, pipe_width=140, gap=280, min_height=50, max_height=440, distance=650):
   pipes = []
   start_x = window_size[0]
   for i in range(count):
       height = randint(min_height, max_height)
       top_pipe = Rect(start_x, 0, pipe_width, height)
       bottom_pipe = Rect(start_x, height + gap, pipe_width, window_size[1] - (height + gap))
       pipes.extend([top_pipe, bottom_pipe])
       start_x += distance
   return pipes

pipes = generate_pipes(150)
pipe_speed = 8
is_touch = False
touch_point_x = int()
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.fill('sky blue')
    draw.rect(window, 'yellow', player_rect)

    for pipe in pipes[:]:
        if not is_touch:
            pipe.x -= pipe_speed
        draw.rect(window, 'green', pipe)
        if pipe.x < -100:
            pipes.remove(pipe)
        if player_rect.colliderect(pipe):
            touch_point_x  = pipe.x
            is_touch = True

    display.update()
    clock.tick(60)

    keys = key.get_pressed()
    if keys[K_w]: player_rect.y -= 5
    if keys[K_s]: player_rect.y += 5

    if is_touch:
        for pipe in pipes[:]:
            pipe.x += 5
        if pipes[0].x > touch_point_x + 150:
            is_touch = False