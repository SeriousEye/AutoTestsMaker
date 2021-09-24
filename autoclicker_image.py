from tkinter import Canvas
import pyautogui, sys
from os import path
import time


# path_ff = path.join('C:\\Users\\pa.kulyasov\\Documents\\python_projects\\PyAutoGUI', 'DD.PNG')


# but = pyautogui.locateOnScreen(path_ff, confidence=0.7)

# pyautogui.doubleClick(but)

# time.sleep(2)

# input_text = pyautogui.locateOnScreen('C:\\Users\\pa.kulyasov\\Documents\\python_projects\\PyAutoGUI\\input_ff.PNG')
# pyautogui.click(input_text)

# # pyautogui.write('lsdfjgs;ldfgj;')
# pyautogui.write('https://test.sbis.ru/mobile_workers')
# pyautogui.press('enter')
# time.sleep(1)

# for i in range(5):
#     im1 = pyautogui.screenshot(f'screen{i}.png', region=(0, 0, 1920, 1040))
    
#     pyautogui.press('pagedown')
#     time.sleep(1)




# x, y = Canvas.create_bitmap

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        # canvas = Canvas.create_bitmap(x, y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')