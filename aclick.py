import re
import pyautogui
import time
import webbrowser

#вспомогательная функция для клика
#кликает когда поймали ссылку на чек
async def click(url):
    if len(re.findall(r'wallet',url)) != 0:
            #когда поймал ссылку ну чек открываем браузер по этой ссылке
            webbrowser.open(url)
            time.sleep(0.8)
            #координаты кнопки в браузере на которую будет нажимать скрипт
            browserX, browserY = 881,487 
            pyautogui.click(browserX, browserY) #клик по кнопке в браузере
            time.sleep(0.6)
            #координаты кнопки в Telegram на которую будет нажимать скрипт
            tgX, tgY = 834,878
            pyautogui.click(tgX, tgY) #клик по кнопке в telegram
            print("SUCCESS")
    else:
        print("NOT FOUND")
