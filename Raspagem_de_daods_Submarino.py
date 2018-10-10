from bs4 import BeautifulSoup
import requests
cont = 1
pesquisa = str(input('Digite um produto para começar a pesquisa:'))
texto_pesquisa = pesquisa

if pesquisa.find(' ') == True:
    url = 'https://www.submarino.com.br/busca?conteudo='+texto_pesquisa.replace(' ','%20')
else:
    url = 'https://www.submarino.com.br/busca?conteudo='+pesquisa
    
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
produtos = soup.findAll('h1',class_='card-product-name')
preços = soup.findAll('span',class_='value')
links = soup.findAll('a',class_='card-product-url')
lista_pro = []
lista_pre = []
lista_links = []

for produto in produtos:
    lista_pro.append(produto.string)
for preço in preços:
    if preço.string != 'R$':
        lista_pre.append(preço.string)
for link in links:
    lista_links.append(link['href'])

for x,y,z in zip(lista_pro,lista_pre,lista_links):
    print('PRODUTO:',x)
    print('PREÇO: R$',y)
    print('LINK: ','https://www.submarino.com.br'+z)
    print('')
    print('')
    print('')
    print('')
    print('')
    
    

sair = str(input('Digite qualquer coisa para sair.'))
