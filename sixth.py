#getting individual channels, awesome merge effect
from PIL import Image

image = Image.open("taylor_swift.jpg")

#separate the colors from an image
r,g,b = image.split()


'''
r,g.show()
g.show()
b.show()
'''

new_img = Image.merge("RGB",(r,g,b))
new_img.show()



#basic transformation
image1 = Image.open("heart.png")
size_image = image1.resize((250,250))
flip_image = image1.transpose(Image.FLIP_TOP_BOTTOM)
spin_image = image1.transpose(Image.ROTATE_90)

size_image.show()
flip_image.show()
spin_image.show()




#modes and filters
from PIL import ImageFilter
image2 = Image.open("taylor_swift.jpg")

#L stands for luminance
black_white  = image2.convert("L")
black_white.show()

blur = image2.filter(ImageFilter.BLUR)
detail = image2.filter(ImageFilter.DETAIL)
edges = image2.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()



#struct
from struct import *

#store as bytes data
#i stands for integer, f stands for float
packed_data = pack('iif',6,19,4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#to get bytes back to normal (b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
original_data = unpack('iif',packed_data)
print(original_data)

print(unpack('iif',b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))



#map
#map provides the function of iterating each value in income list and assign it to dollars
income = [10,30,75]
def double_money(dollars):
    return dollars*2

new_income = list(map(double_money,income))
print(new_income)



#bitwise operators
#Binary AND
a = 50      #110010
b = 25      #011001
c = a & b   #010000
print(c)

#Binary RIGHT SHIFT
x = 240     #11110000
y = x >> 2  #00111100
print(y)


#finding largest or smallest items
import heapq

grades = [32,43,654,34,132,66,99,532]

#the first parameter is to find the top 3 largest
#the second parameter is to get what dataset
print(heapq.nlargest(3,grades))


stocks = [
    {'ticker':'AAPL','price':201},
    {'ticker':'GOOG','price':800},
    {'ticker':'F','price':54},
    {'ticker':'MSFT','price': 313},
    {'ticker':'TUNA','price': 68}
]
print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']))


#dictionary calculations
stocks = {
    'GOOG':434,
    'AAPL':325,
    'FB':54,
    'AMZN':623,
    'F':32,
    'MSFT':549
}

min_price = min(zip(stocks.values(),stocks.keys()))
print(min_price)



#finding most frequent items
from collections import Counter
text = "We hope to one day become the world's leader in free, educational resources. We are constantly "\
        "discovering and adding more free content to the website everyday. There is already an enormous "\
        "amount of resources online that can be accessed for free by anyone in the world, the main issue "\
        "right now is that very little of it is organized or structured in any way. We want to be the "\
        "solution to that problem"

words = text.split()
print(words)

counter = Counter(words)
#the parameter to find the top three most common words
top_three = counter.most_common(3)
print(top_three)



#dictionary multiple key sort
from operator import itemgetter

users = [
    {'fname':'Mary','lname':'Chew'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Williams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'}
]

for x in sorted(users,key=itemgetter('fname','lname')):
    print(x)



#sorting custom objects
from operator import attrgetter

class User:
    def __init__(self,x,y):
        self.name = x
        self.user_id = y

    #__repr__ is a string representation of the User object
    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User('Mary',43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brian', 2),
    User('Joby', 77),
    User('Amanda', 9)
]


for user in sorted(users,key=attrgetter('name')):
    print(user)

print('-----')

for user in sorted(users,key=attrgetter('user_id')):
    print(user)
