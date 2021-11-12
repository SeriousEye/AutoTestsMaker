

class Actions():

    def __init__(self):
        self.all_actions = {
            "Переместить курсор": self.move_mouse()[0],
            "Перетащить мышью": self.drag_mouse()[0],
            "Клик мыши": self.click_mouse()[0],
            "Двойной клик": self.doubleclick_mouse()[0]
        }

    def turn_on_lib(self):
        """Подключается библиотека Pyautogui"""

        return "import pyautogui\n"

    def move_mouse(self, x=0, y=0, duration=0.1):
        """Перемещает курсор на нужные координаты с задержкой по умолчанию 0.1 секунды"""

        return (f"pyautogui.moveTo(x={int(x)}, y={int(y)}, duration={duration})\n", 3)

    def drag_mouse(self, x=0, y=0, duration=0.1, button="left" ):
        """Перетаскивание мышью в нужные координаты"""

        return (f"pyautogui.drag(x={int(x)}, y={int(y)}, duration={duration}, button='{button}')\n", 4)

    def click_mouse(self, x=None, y=None, button="left", clicks=1, interval=0.25):
        """Нажатие кнопки мыши и её отпускание,
        можно какой кнопкой сделать клик - 'left', 'rigth', middle'
        click - количество нажатий
        interval - пауза между нажатиями."""

        return (f"pyautogui.click(x={x}, y={y}, button={button}, clicks={clicks}, interval={interval})\n", 5)

    def doubleclick_mouse(self, x=None, y=None, button="left", interval=0.25):
        """Нажатие кнопки мыши и её отпускание,
        button клик кнопкой мыши - 'left', 'rigth', middle'
        interval - пауза между нажатиями."""

        return (f"pyautogui.click(x={x}, y={y}, button={button}, interval={interval})\n", 4)

# https://pyautogui.readthedocs.io/en/latest/mouse.html