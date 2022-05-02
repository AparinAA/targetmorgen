from telethon import TelegramClient, sync, events
import requests
import webbrowser
import pyautogui
import time
import re
from dotenv import load_dotenv
import os

#читаем env data из файла .env
load_dotenv()

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



#ПОДКЛЮЧЕНИЕ К API TELEGRAM
INPUT_CHANNEL = "alisherhateu" #name channel
INPUT_TEST = 'alxaparin'

api_id = os.getenv("api_id")  #api id == int
api_hash = os.getenv("api_hash") #api hash == string

#Получаем API telegram
client = TelegramClient('session_name', api_id, api_hash)

#Обработчки новых сообщений в канале INPUT_TEST
@client.on(events.NewMessage(chats=(INPUT_TEST)))
async def normal_handler(event):
    print("NEW POST!")
    try:
        #Если поймал кнопку с ссылкой
        url = event.message.reply_markup.rows[0].buttons[0].url
        await click(url)
    except:
        #Если поймал просто текст, то ищем в ней ссылку на wallet
        check_url = re.findall(r'https?://t.me/wallet\S+',event.message.text)
        if len(check_url) != 0:
            url = check_url[0]
            await click(url)
        else:
            print("NOT FOUND URL")

#Обработчки новых сообщений в канале INPUT_CHANNEL
@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):
    print("NEW POST!")
    try:
        #Если поймал кнопку с ссылкой
        url = event.message.reply_markup.rows[0].buttons[0].url
        await click(url)
    except:
        #Если поймал просто текст, то ищем в ней ссылку на wallet
        check_url = re.findall(r'https?://t.me/wallet\S+',event.message.text)
        if len(check_url) != 0:
            url = check_url[0]
            await click(url)
        else:
            print("NOT FOUND URL")

def main():
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
