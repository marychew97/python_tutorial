name = "Mary"

if name is "Bucky":
    print("Hey there Bucky")
elif name is "Lucy":
    print("What up Lucy")
elif name  is"Sammy":
    print("What up Sammy")
else:
    print("Please sign up for the site")


#looping
food = ['bacon','tuna','ham','sausages','beef']
menu = []
for item in food[:2]:
    print(item)
    print(len(item))
    menu.append(item)
print (menu)


for x in range(10):
    print(x)
    print("Mary loves to code")

#5 is the start and 12 is the end
for x in range(5,12):
    print(x)

#10 is the start, 40 is the end, 5 is an increment
for x in range(10,40,5):
    print(x)


x = 5

'''
while x<10:
    print(x)
'''
#this is a single comment

magicNumber = 26

for x in range(101):
    if x is magicNumber:
        print(x, " is a magic number")
        break
    else:
        print(x)

#continue
numbersTaken = [2,5,12,33,17]
print("Here are the numbers that are still available:")
for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)


#functions
def beef():
    print("Dayum, functions are cool!")

def bitcoin_to_usd(btc):
    amount = btc*527
    print(amount)

beef()
bitcoin_to_usd(3.85)
bitcoin_to_usd(13)

def allowed_dating_age(his_age):
    #to calculate how young is a girl for a date
    girls_age = his_age/2 + 7
    return girls_age

guys_limit = allowed_dating_age(27)
print("He can date girls",guys_limit,"or older")


#default argument
def get_gender(sex="Unknown"):  #sex is unknown by default
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()