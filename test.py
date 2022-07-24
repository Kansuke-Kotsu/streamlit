import streamlit as st
from bs4 import BeautifulSoup
#import requests
from urllib.request import urlopen
import numpy as np
from random import random
import random
#import io
from PIL import Image
from email.mime import image
#import base64
import streamlit.components.v1 as stc



st.title("Battle Spirits デッキシミュレーリョン")

def test(URL):
    #URL = "https://club.battlespirits.com/bsclub/mydeck/decksrc/202207/11657463961882_20220710.html"

    # HTMLを解析
    html = urlopen(URL)
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    st.write(URL)

    #変数定義
    head_url = "https://club.battlespirits.com"
    images = []
    card_name = []
    card_counts =[]
    counts =[]
    deck =[]
    n = 0  # 契約スピリット判定用

    # 解析したHTMLから任意の部分のみを抽出
    images = soup.select("main > section > div > ul > li")
    card_name = soup.select("main > section > div > ul > li")

    for i in range(len(images)):
        images[i] = images[i].find("img")
        card_name[i] = card_name[i].find("img")
        if images[i].get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
            images[i] = images[i].get("src")
        if card_name[i].get("alt"):
            card_name[i] = card_name[i].get("alt")

    # 各カードの枚数を取得
    print("---------デッキ情報---------")
    card_counts = soup.find_all('p', class_='cardCount')
    for i in range(len(card_counts)):
        if card_counts[i].string == "1枚":
            counts.append(1)
        elif card_counts[i].string == "2枚":
            counts.append(2)
        else:
            counts.append(3)

    #契約スピリットがいる場合
    for i in range(len(images)):
        if card_name[i] == "相棒竜グロウ" or card_name[i] == "相棒狼ランポ" or card_name[i] == "相棒騎士バット" or card_name[i] == "相棒機スターク" or card_name[i] == "相棒鳥フェニル" or card_name[i] == "相棒鮫シャック":
            keiyaku = images[i]
            counts[i] = counts[i] - 1
            n =1
            break

    # デッキ作成
    for i in range(len(counts)):
        for j in range(counts[i]):
            deck.append(head_url + images[i])

    # シャッフル
    shuffle_deck = deck
    random.shuffle(shuffle_deck)
    if n == 1:
        deck.insert(0, head_url + keiyaku)
    
    col= st.columns(5)
    for i in range(5):
        with col[i]:
            st.image(shuffle_deck[0])
            shuffle_deck.pop(0)



def main():
    URL = st.text_input("URLを入力してください")
    test(URL=URL)
     

        


if __name__ == '__main__':
    main()
    


