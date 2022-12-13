# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sber = ['4279 01','4276 44', '4276 31', '4276 01','5469 55','2202 20','2201 40']
alpha = ['4154 28','4779 64', '4154 28','5486 74','5211 78','2200 45','2202 55']
prom = ['4478 17','4478 18', '4762 08','5547 59','2201 82','2202 12']
center = [14,15,17,20,24,29,34,38,42,46,54,61,66,68,28,78,45]
sever = [86,87,11,55,19,27,41,47,49,58,40,]
sun = [79,82,26,83,85,91,90,96,30,7,12,60,]
volga = [80,88,89,92,94,97,33,22,53,56,57,48,36,63,73]
ural = [37,65,67,74,75]
sibir = [84,81,93,95,13,59,72,25,62,32,50,52,69,76,43]
west = [98,20,51,44,64,99,77]
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
def price(x):
    if x>=1000 and x<=5000:
        return 3000
    if x>=6000 and x<=10000:
        return 8000
    if x>=11000 and x<=15000:
        return 13000
    if x>=16000 and x<=20000:
        return 18000
    return 1000000
def card(x):
    x = x[:7]

    if x in sber:
        return "Сбербанк"
    elif x in alpha:
        return "Альфабанк"
    elif x in prom:
        return "Промбанк"
    return "NULL"
def region(x):
    x = int(x[:2])
    if x in center:
        return "Центральный округ"
    elif x in sever:
        return "Северо-Западный округ"
    elif x in sun:
        return "Южный округ"
    elif x in volga:
        return "Приволжский округ"
    elif x in ural:
        return "Уральский округ"
    elif x in sibir:
        return "Сибирский округ"
    elif x in west:
        return "Дальневосточный округ"
    return "РФ"

boolfio = 1 #обязательно
boolpassid = 1 #обязательно
boolplace = 1
boolprice = 1
boolcard = 1 #обязательно
boolpodavlenie = 1
minK = 7

df = pd.read_csv('database.csv',sep=",",encoding="cp1251")
df1 = df.groupby(df.columns.tolist(), as_index= False).size().reset_index().rename(columns={'size':'kAnonimity'})
print(df1.groupby(['kAnonimity']).size())
print("***********************")
#удаление ФИО
if boolfio:
    df = df.drop(['ФИО'], axis='columns')
# замена серии и номера на регион выдачи паспорта
if boolpassid:
    df['Паспортные данные'] = df["Паспортные данные"].apply(lambda x: region(x))
# удаление данных о месте пассажира за исключением класса
if boolplace:
    df['Вагон Место'] = df["Вагон Место"].apply(lambda x: x[:1])
# приведение цены к средней в диапазоне
if boolprice:
    df['Стоимость'] = df['Стоимость'].apply(lambda x: price(x))
# замена номера карты на банк
if boolcard:
    df['Карта оплаты'] = df['Карта оплаты'].apply(lambda x:card(x))
#группировка по одинаковым строкам с добавленем нового столбца  size с кол-вом повторений уникальной строки
# на выходе в таблице останутся только уникальные строки и у каждой будет указано кол-во повторений этой строки
df = df.groupby(df.columns.tolist(), as_index= False).size().reset_index().rename(columns={'size':'kAnonimity'})
print(df.groupby(['kAnonimity']).size())
print("***********************")
#подавление всех строк у которых k anonimity < 7
if boolpodavlenie:
    print("Общее кол-во записей до подавления:")
    allfirst = sum(df['kAnonimity'])
    print(allfirst)
    print("До подавления уникальных записей:")
    print(df.shape[0])
    df = df.loc[df['kAnonimity'] >=minK]
df = df.drop(['index'], axis='columns')
#Выводит общее кол-во записей исходя из кол-ва повторов каждой Уникальной записи
print("Итогове общее кол-во записей:")
alllast = sum(df['kAnonimity'])
print(alllast)
# выводит кол-во Уникальных записей
print("Конечное кол-во уникальных записей:")
print(df.shape[0])
print("процент подавления %.2f" % float(100-100/allfirst*alllast) + "%")
df.to_csv('filename1.csv',index=False)
