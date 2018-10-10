import telepot
import requests
from bs4 import BeautifulSoup


bot = telepot.Bot('695397146:AAE0I0nBRepNhhSzGOMPdYXupRG4wWseKkA')


def recebendoMsg(msg):
    mensagem = msg['text']
    chatID = msg['chat']['id']
    print(mensagem)

    if mensagem == '/start':
        bot.sendMessage(chatID,"Olá, eu sou o Bot do Preço, fui criado no intuito de ajudar as pessoas a acharem os melhores preços na internet. Digite '/produto' para ativar a função.")
    else:
        if mensagem == "Oi":
            bot.sendMessage(chatID,'Oi')

    if mensagem == '/produto':
        bot.sendMessage(chatID,"Digite o que você deseja comprar:")
        mensagem1 = bot.escuta(produto=msg['text'])
        bot.produto(mensagem1)
        bot.sendMessage(chatID,lista_pro,lista_preço,lista_links)
    

bot.message_loop(recebendoMsg)
while True:
    pass

def escuta (produto=None):
    if produto==None:
        produto = input(">:")
        produto = str(produto)
    return produto


def produto(mensagem1):
    
    cont = 1
    pesquisa = mensagem1
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

    return lista_pro, lista_preço, lista_links

bot.message.loop(produto)
