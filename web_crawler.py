import requests   #request information from world wide web when connecting to Internet
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.nomadicmatt.com/travel-blog/page/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        #to find the text that has elements a, can be also class and id
        for link in soup.findAll("a", {"rel":"bookmark"}):
            href = "https://www.nomadicmatt.com/"+link.get("href")
            title = link.string  #to get the title in string as in html
            #print(href)
            #print(title)
            get_single_item_data(href)
        page+=1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll("h1", {"class":"entry-title"}):
        print(item_name.string) #to get h1, h2, etc, use the method .string
    for link in soup.findAll("a"):
        href = link.get("href")
        print(href)

trade_spider(10)