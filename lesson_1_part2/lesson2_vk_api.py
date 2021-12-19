# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:40:22 2021

@author: Vladimir
"""

#https://vk.com/dev/groups.get


import requests
import json
import pprint

#моя страничка
userid = '177798726'
access_token = ''
version='5.81'
extended = '1' 

r = requests.get('https://api.vk.com/method/groups.get', params= {'user_id' : userid, 'access_token' : access_token, 'v':version, 'extended': extended})

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(r.json())

data = r.json()

for i in data['response']['items']:
   print(F" ID: {i['id']}, Name: {i['name']}")

# Вывод
# ID: 32176202, Name: Alt-Right
# ID: 25232578, Name: РБК
# ID: 90051042, Name: Топ Twitter
# ID: 42744677, Name: Westerly
# ID: 40399920, Name: Спутник и Погром
# ID: 60130670, Name: Регион-70 | Томск
# ID: 28261334, Name: TJ
# ID: 26762265, Name: Томские.ру
# ID: 42899882, Name: ТВ2. Новости Сибири и Томска
# ID: 93250065, Name: Черный список Томска
# ID: 23636659, Name: Дром
# ID: 22781583, Name: DTF
# ID: 91933860, Name: N + 1
# ID: 189503883, Name: Architech
# ID: 203030186, Name: Компартия Китая 红龙习近平
# ID: 46758722, Name: Virginia Bēowulf · English Studies
# ID: 20225241, Name: Тинькофф
# ID: 118643747, Name: Платиновые мюсли юных либерах
# ID: 54530371, Name: Библиотека программиста
# ID: 76875894, Name: Райффайзенбанк Россия
# ID: 172432646, Name: Ремонт компьютеров ВАФИКС | Томск
# ID: 169934613, Name: KARPOV.COURSES
# ID: 201452090, Name: Шлепа
# ID: 94208167, Name: Data Mining | Анализ Данных
# ID: 139749780, Name: F
# ID: 41342606, Name: i2HARD.RU
# ID: 39447662, Name: iXBT.com
# ID: 145527688, Name: Syncretis
# ID: 131342114, Name: Kryptex
# ID: 181246839, Name: czar.tv
# ID: 60511457, Name: Медач | Medical Channel
# ID: 64547346, Name: ASRock Россия
# ID: 23242408, Name: Альфа-Банк
# ID: 29354345, Name: Институт биоинформатики
# ID: 58238796, Name: Барахолка электроники и мебели в Томске
# ID: 71479743, Name: Бизнес-инкубатор ТГУ
# ID: 76229642, Name: Роскомнадзор
# ID: 84237348, Name: Марсэль Гайнутдинов (Дневник сетевика)
# ID: 86678270, Name: Студия Аналитики
# ID: 96786501, Name: Храни Деньги! Блог практичного инвестора
# ID: 98210264, Name: Абстрактный Юмор 2.0
# ID: 107824202, Name: Российский научный фонд
# ID: 109394968, Name: Додо Пицца Сочи-Адлер
# ID: 117853995, Name: Блог о надежных инвестициях - InvestBase
# ID: 131489096, Name: Memes on Machine Learning for Young Ladies
# ID: 155982636, Name: Анастасия Лосева | Томск | Украшения | Чокеры
# ID: 171548544, Name: Direct Auto - автоподбор в Томске
# ID: 172806574, Name: M-Technics. Компьютерный энтузиазм.
# ID: 185413393, Name: VK Hackathon | Tomsk
# ID: 194672896, Name: Britain First
# ID: 194753960, Name: Белый угнетатель

