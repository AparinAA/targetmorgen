from telethon import TelegramClient, sync, events
import requests
import time
import re
from dotenv import load_dotenv
import os
from aclick import click

#читаем env data из файла .env
load_dotenv()

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
