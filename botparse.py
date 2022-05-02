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

#Названия каналов, за которыми нужно следить
NAME_CHANNELS = (
    "alisherhateu", #Morgen
    "nemorgenshtern", #NEMORGEN news
    'Full_Time_Trading', #FULL trading news
    'litvintm', #Litvin
    'toncoin_rus', #toncoin_news
    'bogachnaprokach', #Lana
    'wallet_news', #Wallet news
    'tonwhalesnews', #WHALES news
    'durov', #Durov
    'slavamarlow', #Slava Marlow
    'alxaparin', #test account
)

#В этом словаре будут храниться связь ID : nameChannel
name_id_dict = {}

#API id, hash
api_id = os.getenv("api_id")  #api id == int
api_hash = os.getenv("api_hash") #api hash == string

#Получаем API telegram
client = TelegramClient('session_name', api_id, api_hash)

#Обработчки новых сообщений в канале NAME CHANNELS
@client.on(events.NewMessage(chats=NAME_CHANNELS))
async def normal_handler(event):
    print(event.message.date, "\t  | \t\t", name_id_dict[event.message.chat.id], end='\t\t|\t')
    try:
        #Если поймал кнопку с ссылкой
        url = event.message.reply_markup.rows[0].buttons[0].url
        await click(url)
    except:
        #Если поймал просто текст, то ищем в ней ссылку на wallet
        check_url = re.findall(r'https?://t.me/wallet\?\S+',event.message.text)
        if len(check_url) != 0:
            url = check_url[0]
            await click(url)
        else:
            print("NOT FOUND URL")
            print("-"*103)

def main():
    
    #стартуем и проверяем обновления
    client.start()

    #соберем ID каналов и положим в словарь name_id_dict
    print("Channel names which we parse : ")
    for name in NAME_CHANNELS:
        for msg in client.get_messages(name, limit=1):
            print('NAME: {}, ID: {}'.format(name,msg.chat.id))
            name_id_dict[msg.chat.id] = name
    
    print('')
    print("="*103)
    print('DATE NEW POST\t\t\t  | \t\t NAME CHANNEL\t\t|\t RESULT')
    print("-"*103)
    #работаем до момента отключения
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
