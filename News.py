import bs4
from tkinter import *
from bs4 import BeautifulSoup4 as soup
from urllib.request import urlopen
from GoogleNews import GoogleNews
# from newspaper import Article
import pandas as pd

def News():
    root = Tk()
    root.title("Register for TradePay:")
    root.geometry("550x540+0+0")

    frame1 = Frame(root)
    frame1.grid()

    frame2 = Frame(frame1, width=550, height=50, padx=10, pady=5, relief=RIDGE)
    frame2.grid(row=0, column=0)

    # googlenews = GoogleNews(start='05/01/2020', end='05/31/2020')
    # googlenews.search('Jobs')
    # googlenews.result()
    # result = googlenews.get_texts()
    # df = pd.DataFrame(result)

    # fetching live new
    news_url = "https://news.google.com/rss"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = soup(xml_page, "xml")
    news_list = soup_page.find_all("item")
    for news in news_list :
       # if (news.title.news == "job") :
            print(news.title.text)
            print(news.pubDate.text)
            print("_" * 60)

    # fetched live news

    lblTradePay = Label(frame2, text='Live News:', font=('arial', 14, 'bold'))
    lblTradePay.grid(row=0, column=0, sticky=W)
