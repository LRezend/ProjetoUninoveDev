import requests
import csv
from bs4 import BeautifulSoup

print('')
print('')

print('================================================================')
num_of_img = int(input('       Quantas imagens voce deseja fazer o download? '))
print('================================================================')

print('')
print('')

print('================================================================')
directory = str(input('            Diretorio: '))
print('================================================================')

links_lists = []
img_list = []
img_index = 0
page_number = (num_of_img // 20) * 20

with open("entrada.csv.csv", "r") as entrada:
    search = csv.reader(entrada, delimiter=';')
    for linha in search:
        print(linha)


url1 = f'https://www.google.com/search?q={linha}&hl=pt-BR&gbv=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwipwcKTxOfrAhUUDrkGHZ3kB5kQ_AUoAXoECB8QAw&sfr=gws&sei=g8xeX6WWO4KI5OUP1Ne2sAQ'

req = requests.get(url1)
soup = BeautifulSoup(req.text, 'html.parser')

for img in soup.find_all('img')[1:]:
    if img_index == num_of_img:
        break
    else:
        links_lists.append(img.get('src'))
        img_index += 1

for links in links_lists:
    img_list.append(requests.get(links))


for i, img in enumerate(img_list):
    with open(f'{directory}/{linha}_{i}.png', 'wb') as f: #wb = write byte
        f.write(img.content)


print("")
print("                 FIM DO PROGRAMA, VOLTE SEMPRE !")


