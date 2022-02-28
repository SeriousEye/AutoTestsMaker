from os import path

class Actions():

    def __init__(self):
        """При вызове класса инициализируются все действия."""
        self.all_actions = {
            "Переместить курсор": self.move_mouse(),
            "Перетащить мышью": self.drag_mouse(),
            "Клик мыши": self.click_mouse(),
            "Двойной клик": self.doubleclick_mouse(),
            "Ввести текст": self.write_text(),
            "Нажать клавишу": self.press_button(),
            "Скролл": self.scroll_mouse(),
            "Ждать": self.wait_time()
        }

    def turn_on_lib(self):
        """Подключается библиотека Pyautogui и time с методом sleep."""

        return "from PIL import ImageGrab\nfrom functools import partial\nfrom time import sleep\nimport pyautogui\n\n"


    def move_mouse(self, x=0, y=0, duration=0.1):
        """Перемещает курсор на нужные координаты с задержкой по умолчанию 0.1 секунды"""

        return f"pyautogui.moveTo(x={int(x)}, y={int(y)}, duration={duration})\n"


    def drag_mouse(self, x=0, y=0, duration=0.1, button="left" ):
        """Перетаскивание мышью в нужные координаты"""

        return f"pyautogui.drag(x={int(x)}, y={int(y)}, duration={duration}, button='{button}')\n"


    def click_mouse(self, x=None, y=None, button="left", clicks=1, interval=0.25):
        """Нажатие кнопки мыши и её отпускание,
        можно какой кнопкой сделать клик - 'left', 'rigth', middle'
        click - количество нажатий
        interval - пауза между нажатиями."""

        return f"pyautogui.click(x={x}, y={y}, button='{button}', clicks={clicks}, interval={interval})\n"
        

    def doubleclick_mouse(self, x=None, y=None, button="left", interval=0.25):
        """Нажатие кнопки мыши и её отпускание,
        button клик кнопкой мыши - 'left', 'rigth', middle'
        interval - пауза между нажатиями."""

        return f"pyautogui.click(x={x}, y={y}, button='{button}', interval={interval})\n"

    def scroll_mouse(self, scroll=0, x=None, y=None):
        """Скролл колесом мыши, вверх - положительное целое число,
        вниз - отрицательное целое число. scroll - количество щелчков,
        x и y перемещают курсор в позицию для скролла."""

        return f"pyautogui.scroll({scroll}, x={x}, y={y})\n"

    def write_text(self, text="", interval=0.1):
        """Вводит тест поле с установленным курсором."""

        return f"pyautogui.write('{text}', interval={interval})\n"

    def press_button(self, name_button='enter'):
        """Инициирует нажатие клавиши клавиатуры"""

        return f"pyautogui.press('{name_button}')\n"

    def wait_time(self, wait=1):
        """Инициирует ожидание."""

        return f"sleep({wait})\n"

    def screenshot(self, region=(0, 0, 0, 0), name1="", name2=""):
        "Делает скриншот области экрана."

        x1, y1, x2, y2 = region
        

        wx, hy = x2, y2
        # half_screen = int(wx/2)
        path_to_screen = path.join(name1, name2).replace("\\", r"\\")

        # if 0 <= int(x1) < half_screen and 0 <= int(y1) <= hy:
        if x1 == 0 and y1 == 0:
            return f"""ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)\npyautogui.screenshot("{path_to_screen}.png", region=(0, 0, {x2}, {y2}))\n"""
            # pyautogui.screenshot(f'{name1}_{name2}.png', region=(0, 0, half_screen, hy))
            # print("file left screen saved!")
        # elif half_screen <= int(x1) < wx and 0 <= int(y1) <= hy:
        else:
            return f"""ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)\npyautogui.screenshot("{path_to_screen}.png", region=({x1}, 0, {x2}, {y2}))\n"""
            # pyautogui.screenshot(f'{name1}_{name2}.png', region=(half_screen, 0, half_screen, hy))
            # print("file right screen saved!")

        



# https://pyautogui.readthedocs.io/en/latest/mouse.html