# zaebot
Периодически читает ленту одного пользователя, дёргает оттуда существительные, относительно удачно склоняет подставляемое к ним слово "заебали" и постит это от второго пользователя.

Периодически удаляет те твиты, которые не набрали ни одного fav / rt.

## Конфиг
- common - настройки приложения
- reader - пользователь, ленту которого будем читать
- writer - бот, от имени которого будем постить

## Идеи
- Стоит перенести в конфиг некоторые параметры, например подставляемые слова, количество слов за пост и частоту постинга, но мне лениво.
- Чёрный список для слов. (лол, итд)

## usage
После вбивания параметров в конфиг:

    cd папка_с_проектом && setsid python bot.py &>/dev/null & disown -a

## первое воплощение

https://twitter.com/vsevsezaebali
