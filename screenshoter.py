from PIL import ImageGrab
from functools import partial
import pyautogui


class ScreenShot():

    def __init__(self) -> None:
        pass

    def fullscreenshot():
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        img = ImageGrab.grab()
        wx, hy = img.size


        im1 = pyautogui.screenshot(f'temp_screen.png', region=(0, 0, wx, hy))

#add test comment
