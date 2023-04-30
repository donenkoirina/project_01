# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
songs = random.sample(my_favorite_songs, 3)
total_time = 0
for song in songs:
    total_time += song[1]

print(f"Три песни звучат {total_time:.2f} минут")


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
import random
songs = random.sample(list(my_favorite_songs_dict.keys()), 3)
total_time = 0
for song in songs:
    total_time += my_favorite_songs_dict[song]
print(f"Три песни звучат {total_time:.2f} минут.")



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random

random_songs = random.sample(my_favorite_songs, 3)
for song in random_songs:
    print(f"Случайная песня: {song[0]} ({song[1]} минут)")

import random

random_song = random.sample(my_favorite_songs, 1)
print(f"Случайная песня: {random_song[0][0]}")


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
import datetime
songs_with_time_format = []
for song in my_favorite_songs:
    title, duration = song
    minutes, fraction = divmod(duration, 1)
    seconds = fraction * 60
    time_object = datetime.time(int(minutes), int(seconds))
    songs_with_time_format.append([title, time_object])
for song in songs_with_time_format:
    title, time_object = song
    time_string = time_object.strftime("%H:%M")
    print(title, time_string)