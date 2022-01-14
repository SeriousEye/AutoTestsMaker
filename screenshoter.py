from PIL import ImageGrab, Image
from functools import partial
import pyautogui


class ScreenShot():

    def __init__(self) -> None:
        self.wx = None
        self.hy = None

    def fullscreenshot(self):
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        img = ImageGrab.grab()
        wx, hy = img.size


        im1 = pyautogui.screenshot(f'temp_screen.png', region=(0, 0, wx, hy))

    def rectangle_screenshot(self, start_x, start_y, end_x, end_y):
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        img = ImageGrab.grab((start_x, start_y, end_x, end_y))
        img.save("temp.png", "PNG")

    def screen_size(self, value_x, value_y, path, name1, name2):
        if value_x != 0 and value_y != 0:
            ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

            img = ImageGrab.grab()
            wx, hy = img.size
            half_screen = int(wx/2)

            if 0 <= int(value_x) < half_screen and 0 <= int(value_y) <= hy:
                pyautogui.screenshot(f'{name1}_{name2}.png', region=(0, 0, half_screen, hy))
                print("file left screen saved!")
            elif half_screen <= int(value_x) < wx and 0 <= int(value_y) <= hy:
                pyautogui.screenshot(f'{name1}_{name2}.png', region=(half_screen, 0, half_screen, hy))
                print("file right screen saved!")
        else:
            pass


        # return (0, 0, half_screen, hy), (half_screen, 0, wx, hy)

# a = ScreenShot().rectangle_screenshot(0, 500, 500, 700)
# a = ScreenShot()

# print(a.screen_size())





#add test comment
