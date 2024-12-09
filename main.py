import math
from PIL import ImageGrab, ImageOps
import pyautogui
import keyboard
import time
import numpy as np

WINDOW_WIDTH = 1420
WINDOW_HEIGHT = 400
WINDOW_TOP = 350
WINDOW_LEFT = 0

last_update = 0
elapsed_time = 0
jump_count = 0

def get_pixel(image, x, y):
    px = image.load()
    return px[x, y]

GROUND_LEVEL = 300
AIR_LEVEL = 275
SEARCH_START = 430
SEARCH_END = 450

time.sleep(2)
while True:
    start_time = time.time()

    if math.floor(elapsed_time) != last_update:
        SEARCH_END += 5
        if SEARCH_END >= WINDOW_WIDTH:
            SEARCH_END = WINDOW_WIDTH
        last_update = math.floor(elapsed_time)

    screenshot = pyautogui.screenshot(region=(WINDOW_LEFT, WINDOW_TOP, WINDOW_WIDTH, WINDOW_HEIGHT))
    bg_color = get_pixel(screenshot, 435, 30)

    for x in reversed(range(SEARCH_START, SEARCH_END)):
        if get_pixel(screenshot, x, GROUND_LEVEL) != bg_color or get_pixel(screenshot, x, AIR_LEVEL) != bg_color:
            keyboard.press(' ')
            jump_count += 1
            break

    elapsed_time += time.time() - start_time
    print(f"Tiempo: {elapsed_time:.2f}s, Saltos: {jump_count}")
