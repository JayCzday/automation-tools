import pyautogui
import time
import xlrd
import pyperclip

save_path='H:\\pythonProject\\test\\savepath\\'
i=1
symbol_location=pyautogui.locateCenterOnScreen('./img/symbol.png',confidence=0.9)
pyautogui.click(symbol_location.x-50, symbol_location.y+50, clicks=1, interval=0.2, duration=0.2, button='left')
while(i<10):
    print(i)
    pyautogui.hotkey('alt','a')
    pyautogui.click()
    save_location=pyautogui.locateCenterOnScreen('./img/save3.png',confidence=0.9)
    pyautogui.click(save_location.x-10,save_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
    #symbol2_location = pyautogui.locateOnScreen('./symbol2.png', confidence=0.3)
    pyautogui.click(200, 450, clicks=1, interval=0.2, duration=0.2, button='left')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    inputValue=save_path+str(i)
    print(inputValue)
    pyautogui.click(200, 450, clicks=1, interval=0.2, duration=0.2, button='left')
    pyperclip.copy(inputValue)
    pyautogui.hotkey('ctrl', 'v')
    #save2_location = pyautogui.locateCenterOnScreen('./img/save2.png', confidence=0.9)
    pyautogui.click(800, 500, clicks=1, interval=0.2, duration=0.2, button='left')
    pyautogui.click(symbol_location.x - 50, symbol_location.y + 100, clicks=1, interval=0.2, duration=0.2, button='left')
    pyautogui.scroll(-120000)
    time.sleep(0.1)
    i=i+1


