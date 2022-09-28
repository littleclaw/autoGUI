import time

import pyautogui

screenWidth, screenHeight = pyautogui.size()
if __name__ == '__main__':
    pyautogui.hotkey('win', 'd')
    print(screenWidth, screenHeight)
    pyautogui.moveTo(screenWidth - 40, screenHeight / 2, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.rightClick()
    pyautogui.moveRel(20, 20)
    pyautogui.click()
    # subprocess.call("cd /d C:\\Users\\EDZ\\Desktop")
    txtFilePath = 'C:\\Users\\EDZ\\Desktop\\hiahia.txt'
    txtFile = open(txtFilePath, 'w')
    txtFile.close()
    time.sleep(2)
    pyautogui.hotkey('win', 'r')
    pyautogui.getWindowsWithTitle('运行')[0].activate()
    pyautogui.press('enter')
    pyautogui.write("notepad " + txtFilePath, interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    notepadWindow = pyautogui.getWindowsWithTitle('记事本')[0]
    notepadWindow.activate()
    pyautogui.write("PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with "
                    "other applications. The API is designed to be simple. PyAutoGUI works on Windows, macOS, "
                    "and Linux, and runs on Python 2 and 3.", interval=0.2)
    pyautogui.hotkey('ctrl', 's')
    notepadWindow.close()
