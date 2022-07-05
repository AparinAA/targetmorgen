# BotParse

**Скрипт для мониторинга ссылок на чек от бота Wallet в Telegram.**  
**Обработка этой ссылки и поочередное кликанье по ссылкам для активации приложения**

## Для запуска

**Основные переменные**

Для подключения к Telegram API:
```
api_id=int  
api_hash=string
```
Эти переменные добавляются в файл .env

Для полечения этих данных api:

1. Заходим на сайт https://my.telegram.org/apps
2. Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.


Названия канала и тестовый (свой канал или ссылка на себя), которые будут парсится для поиска чека
```
NAME_CHANNELS = ('namechannel_1','namechannel_2,'nametest')
ID_CHANNELS = (id_int_1, id_int_2, ...)
```

Пример названия канала или имя аккаунта из ссылки: t.me/**namechannel**

Последние важнные переменные

Эти переменные нужны для определения положения (координат) кнопки в браузере "*Разрешить/Открыть в приложение telegram*" или чего-то аналогичного и для определения положения кнопки "*Начать/Start*" в Telegram (она появляется у бота вместо "*Поля ввода текста*")

*aclick.py*  
Для Браузера `browserX, browserY = int, int`  
Для Telegram `tgX, tgY = int, int`

Они находятся в функции `async def click(...)` и определяются индивидуально для каждого экрана с помощью функции из библиотеки **pyautogui**
```
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
```

Запуск `python botparse.py`
