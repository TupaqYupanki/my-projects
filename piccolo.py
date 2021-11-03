import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl import Workbook

#Читаем книгу
wb = load_workbook('Мониторинг_цены_и_акции_конкурентов.xlsx')

#делаем активной 2ую страницу
wb.active = 1
ws = wb.active

#ws.cell(row=4, column=3).value - зачение ячейки

y = 1
for row in ws.iter_rows(min_row=1, min_col=3, max_col=3, max_row=200, values_only=True):
 for value in row:
  if 'https' in str(value):
      piccolo = str(value)
      print(piccolo)
      url = requests.get(piccolo)
      soup = BeautifulSoup(url.content)
      mydivs = soup.find_all("span", class_= "ty-price-num")
      ws.cell(row=y, column=20).value = mydivs[0].text
      y=y+1
  else: y=y+1

z = 1
for row in ws.iter_rows(min_row=1, min_col=5, max_col=5, max_row=200, values_only=True):
 for value in row:
  if 'konfigurator' in str(value): z=z+1
  elif 'https' in str(value):
      lapsi = str(value)
      print(lapsi)
      url = requests.get(lapsi, headers={'User-Agent':'Test'})
      soup = BeautifulSoup(url.content)
      mydivs = soup.find_all("div", class_= "price")[0]
      # print(mydivs.contents[0])
      ws.cell(row=z, column=21).value = mydivs.contents[0]
      z=z+1
  else: z=z+1

t = 1
for row in ws.iter_rows(min_row=1, min_col=9, max_col=9, max_row=200, values_only=True):
 for value in row:
   if 'https' in str(value):
        olant = str(value)
        print(olant)
        url = requests.get(olant)
        soup = BeautifulSoup(url.content)
        mydivs = soup.find("div", class_= "card-price__current")
        ws.cell(row=t, column=22).value = str(mydivs.text)[:-5]
        t=t+1
   else: t=t+1

a = 1
for row in ws.iter_rows(min_row=1, min_col=13, max_col=13, max_row=200, values_only=True):
 for value in row:
  if 'konstruktor' in str(value): a=a+1
  elif 'https' in str(value):
        akusher = str(value)
        print(akusher)
        akusherId = akusher.split('/')[4].split('-')[0]
        url = requests.get(akusher)
        soup = BeautifulSoup(url.content)
        mydivs = soup.find("span", id="tovar_price_"+str(akusherId))
        ws.cell(row=a, column=23).value = str(mydivs.text)
        a=a+1
  else: a=a+1


wb.save('test.xlsx')
