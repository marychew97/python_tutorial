import second
import random
import urllib.request
from urllib import request

second.fish()

x = random.randrange(1,1000)
print(x)


#download image from web
def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/68dd54ca-60cf-4ef7-898b-26d7cbe48ec7/10-dithering-opt.jpg")


#read and write files
fw = open("sample.txt","w") #w means open a file and write to it
fw.write("writing some stuff in my text file\n")
fw.write("I like bacon\n")
fw.close()

fr = open("sample.txt","r") #r means to read the file
text = fr.read() #read the data and assign it to the variable text
print(text)
fr.close()


#download csv files from web
goog_url="http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
def download_stock_data(csv_url):
    response = request.urlopen(csv_url) #open url of a csv file and is stored in response
    csv = response.read() #read data
    csv_str = str(csv)
    lines = csv_str.split("\\n") #split the data with new lines
    dest_url = r"goog.csv"  #r means raw
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)