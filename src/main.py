from time import sleep
from random import randint
from pyautogui import moveRel, position, Point

while True:
    try:
        curr: Point = position()
        print(f'x={curr.x}, y={curr.y}')
        x: int = randint(-50, 50)
        y: int = randint(-50, 50)
        moveRel(x, y, 2)
        sleep(2)
    except:
        break
