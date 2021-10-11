from PIL import ImageGrab, Image
from functools import partial
import pyautogui


class ScreenShot():

    def __init__(self) -> None:
        pass

    def fullscreenshot(self):
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        img = ImageGrab.grab()
        wx, hy = img.size


        im1 = pyautogui.screenshot(f'temp_screen.png', region=(0, 0, wx, hy))

    def rectangle_screenshot(self, start_x, start_y, end_x, end_y):
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        img = ImageGrab.grab((start_x, start_y, end_x, end_y))
        img.save("temp.png", "PNG")

# a = ScreenShot().rectangle_screenshot(0, 500, 500, 600)





#add test comment
