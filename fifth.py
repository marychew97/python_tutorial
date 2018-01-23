#unpack list or tuples
#date refers to December 23,2015
#name refers to Bread Gloves
#price refers to 8.51
date,name,price = ["December 23, 2015","Bread Gloves", 8.51]
print(price)

def drop_first_last(grades):
    #*middle is including all grades except first and last
    first,*middle,last = grades
    avg = sum(middle)/len(middle)
    print(avg)

#76,98 and 54 are in middle which is *middle
drop_first_last([65,76,98,54,21])
drop_first_last([65,76,98,100,21,93,54,21])



#zip function
first = ["Mary","Tom","Taylor"]
last = ["Chew","Hanks","Swift"]

#tie both first and last together and store it into names
names = zip(first,last)

for a,b in names:
    print(a,b)



#lambda
answer = lambda x: x*7

#to pass the number 5 to x using lambda
print(answer(5))



#min,max and sorting dictionaries
stocks = {
    "GOOG" : 520.54,
    "FB" : 76.45,
    "YHOO" : 39.28,
    "AMZN" : 306.21,
    "AAPL" : 99.76
}

#find the minimum value
print(min(zip(stocks.values(),stocks.keys())))

#find the maximum value
print(max(zip(stocks.values(),stocks.keys())))

#sort out the entire dictionary
print(sorted(zip(stocks.values(),stocks.keys())))



#Pillow, cropping image
from PIL import Image

img = Image.open("taylor_swift.jpg")
#based on coordinates
#x0,y0,x1,y1
area = (100,100,500,500)
cropped_img = img.crop(area)
print(img.size)
print(img.format)

#create a temporary image file
cropped_img.show()



#combine images together
taylor = Image.open("taylor_swift.jpg")
heart = Image.open("heart.png")

#make sure the image to be pasted is the same size to prevent off the taylor image
area = (0,0,300,279)
taylor.paste(heart,area)
taylor.show()