import sys, time
import requests as req
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from mainSettings import *
from tgBot import telegramBot

name = ''
prise = '' 
m2 = ''
link = ''
linkSalesman = ''

def parsingDataCian():
    for i in tqdm(range(100), ascii=True, desc='parsing_html', ncols=80):
        time.sleep(0.01)
    r = req.get(url, params=payload)
    print('parsing html successful!')
    time.sleep(1)
    
    if r.status_code == 200:
        for i in tqdm(range(100), ascii=True, desc='exam_connect', ncols=80):
            time.sleep(0.01)
        print('successful connection!')
        time.sleep(1)
    elif r.status_code != 200:
        for i in tqdm(range(100), ascii=True, desc='exam_connect', ncols=80):
            time.sleep(0.01)
        print('failed connection...')
        time.sleep(1)
        sys.exit()

    soup = bs(r.content, 'lxml')
    items = soup.find_all('div', class_='_93444fe79c--card--2umme _93444fe79c--promoted--62c4a')
    dataSafe = []

    for item in items:
        dataSafe.append(
            {
        'name': item.find_next('div', class_='_93444fe79c--container--JdWD4').find('span').get_text(strip=True),
        'prise': item.find_next('span', class_='_93444fe79c--color_black_100--A_xYw _93444fe79c--lineHeight_28px--3QLml _93444fe79c--fontWeight_bold--t3Ars _93444fe79c--fontSize_22px--3UVPd _93444fe79c--display_block--1eYsq _93444fe79c--text--2_SER _93444fe79c--text_letterSpacing__normal--2Y-Ky').find('span').get_text(strip=True),
        'm2': item.find_next('p', class_='_93444fe79c--color_gray60_100--3VLtJ _93444fe79c--lineHeight_20px--2dV2a _93444fe79c--fontWeight_normal--2G6_P _93444fe79c--fontSize_14px--10R7l _93444fe79c--display_block--1eYsq _93444fe79c--text--2_SER _93444fe79c--text_letterSpacing__normal--2Y-Ky').get_text(strip=True),
        'link': item.find_next('a', class_='_93444fe79c--link--39cNw').get('href'),
        'linkSalesman': item.find_next('a', class_='_93444fe79c--jk--YYtNL').get('href')
            }
        )

    for i in tqdm(range(100), ascii=True, desc='read_data', ncols=80):
        time.sleep(0.01)
    print('data read successfully!')
    time.sleep(1)

    global name, prise, m2, link, linkSalesman

    for i in dataSafe:
        name = i['name']
        print(name)
        prise = i['prise']
        print(prise)
        m2 = i['m2']
        print(m2)
        link = i['link']
        print(link)
        linkSalesman = i['linkSalesman']
        print(linkSalesman)

    for i in tqdm(range(100), ascii=True, desc='call_data_tg', ncols=80):
        time.sleep(0.01)
    print('sending data successfully!')
    time.sleep(1)

parsingDataCian()
telegramBot(name, prise, m2, link, linkSalesman)
