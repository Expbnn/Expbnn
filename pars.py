import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def kategory0():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/akushersko-ginekologicheskie-i-protivomastitnye-prep"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory1():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/antibakterialnye-preparaty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory2():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/antigelmintnye-i-protivoparazitarnye-preparaty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory3():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/vaktsiny-i-syvorotki"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory4():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/vitamino-mineralnye-preparaty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory5():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/gepatoprotektory"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory6():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/gomeopaticheskie-preparaty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory7():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/gormonalnye-preparaty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory8():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/dezinfektsiya-dezinsekitsya-deratizatsiya"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory9():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/immunomodulyatory"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory10():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/insektoakaritsidnye-preparaty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory11():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/instrumenty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory12():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/koktsidiostatiki"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory13():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/mazi-krema-sprei"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory14():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/preparaty-dlya-regulyatsii-polovoi-okhoty"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
def kategory15():
    list=[]
    URL_TEMPLATE = "http://kormvet.kz/categories/sredsta-simptomaticheskoi-terapii"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'lxml')
    cat = soup.find_all('a', class_='products-view-name-link')
    prc = soup.find_all('div', class_='price-number')
    for i in range(0, len(cat)):
        for i in range(0, len(prc)):
            list.append(cat[i].text + '  цена ' + prc[i].text + ' тенге')
    return list
                    
                