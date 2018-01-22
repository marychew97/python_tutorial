import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"html.parser")
    for post_text in soup.findAll("p"):
        content = post_text.string

        #to prevent the AttributeError to happen
        if content is not None:
            words = content.lower().split()  # lower case everything and split sentences into words
            for each_word in words:
                print(each_word)
                word_list.append(each_word)
    clean_up_list(word_list)

#to remove any symbols
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+{}|:?><`-=';,./[]\\\'\""
        for i in range(0,len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word)>0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #itemgetter is 1 because it refers to value whereas itemgetter is 0 because it refers to key
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key,value)

start("http://www.health.com/beauty/model-iskra-lawrence-body-positivity-instagram")

