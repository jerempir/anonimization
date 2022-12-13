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
# ����� ����������� �� ����� ��������
pd.set_option('display.max_columns', None)
# ����� ����������� �� ���������� �������� � ������
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
        return "��������"
    elif x in alpha:
        return "���������"
    elif x in prom:
        return "��������"
    return "NULL"
def region(x):
    x = int(x[:2])
    if x in center:
        return "����������� �����"
    elif x in sever:
        return "������-�������� �����"
    elif x in sun:
        return "����� �����"
    elif x in volga:
        return "����������� �����"
    elif x in ural:
        return "��������� �����"
    elif x in sibir:
        return "��������� �����"
    elif x in west:
        return "��������������� �����"
    return "��"

boolfio = 1 #�����������
boolpassid = 1 #�����������
boolplace = 1
boolprice = 1
boolcard = 1 #�����������
boolpodavlenie = 1
minK = 7

df = pd.read_csv('database.csv',sep=",",encoding="cp1251")
df1 = df.groupby(df.columns.tolist(), as_index= False).size().reset_index().rename(columns={'size':'kAnonimity'})
print(df1.groupby(['kAnonimity']).size())
print("***********************")
#�������� ���
if boolfio:
    df = df.drop(['���'], axis='columns')
# ������ ����� � ������ �� ������ ������ ��������
if boolpassid:
    df['���������� ������'] = df["���������� ������"].apply(lambda x: region(x))
# �������� ������ � ����� ��������� �� ����������� ������
if boolplace:
    df['����� �����'] = df["����� �����"].apply(lambda x: x[:1])
# ���������� ���� � ������� � ���������
if boolprice:
    df['���������'] = df['���������'].apply(lambda x: price(x))
# ������ ������ ����� �� ����
if boolcard:
    df['����� ������'] = df['����� ������'].apply(lambda x:card(x))
#����������� �� ���������� ������� � ���������� ������ �������  size � ���-��� ���������� ���������� ������
# �� ������ � ������� ��������� ������ ���������� ������ � � ������ ����� ������� ���-�� ���������� ���� ������
df = df.groupby(df.columns.tolist(), as_index= False).size().reset_index().rename(columns={'size':'kAnonimity'})
print(df.groupby(['kAnonimity']).size())
print("***********************")
#���������� ���� ����� � ������� k anonimity < 7
if boolpodavlenie:
    print("����� ���-�� ������� �� ����������:")
    allfirst = sum(df['kAnonimity'])
    print(allfirst)
    print("�� ���������� ���������� �������:")
    print(df.shape[0])
    df = df.loc[df['kAnonimity'] >=minK]
df = df.drop(['index'], axis='columns')
#������� ����� ���-�� ������� ������ �� ���-�� �������� ������ ���������� ������
print("������� ����� ���-�� �������:")
alllast = sum(df['kAnonimity'])
print(alllast)
# ������� ���-�� ���������� �������
print("�������� ���-�� ���������� �������:")
print(df.shape[0])
print("������� ���������� %.2f" % float(100-100/allfirst*alllast) + "%")
df.to_csv('filename1.csv',index=False)
