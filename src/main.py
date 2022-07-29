from sys import argv
from time import sleep
from random import randint
from typing import Tuple, Union
from pyautogui import moveRel, position, Point, click, moveTo
# 344x1049

clickable: Union[Tuple[int, int], None] = None
pause: float = 2.

if len(argv) > 1:
    try:
        clickable = (int(argv[-2], base=10), int(argv[-1], base=10))
        pause = 20.
    except:
        pass

while True:
    try:
        curr: Point = position()
        print(f'x={curr.x}, y={curr.y}')
        if clickable is not None:
            moveTo(clickable[0], clickable[1], 5)
            click(clicks=2, interval=2.)
            moveTo(curr.x, curr.y, 5)
        else:
            x: int = randint(-50, 50)
            y: int = randint(-50, 50)
            moveRel(x, y, 2)
        sleep(pause)
    except:
        break
