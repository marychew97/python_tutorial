#keyword arguments
def dumb_sentence(name="Bucky",action="ate",item="tuna"):
    print(name, action, item)

dumb_sentence()
dumb_sentence("Sally","farts","gently")
dumb_sentence(item="awesome",action="is")


#flexible number of arguments
def add_numbers(*args):   #to get any number of arguments
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3,32)
add_numbers(3,43,5453,354234,463463)


#unpacking arguments
def health_calculator(age,apples_ate,cigs_smoked):
    answer = (100-age)+(apples_ate*3.5)-(cigs_smoked*2)
    print(answer)

mary_data = [21,10,0]
health_calculator(mary_data[0],mary_data[1],mary_data[2])
health_calculator(*mary_data) #unpacking arguments


groceries={"cereal","milk","starcrunch","beer","duct_tape","lotion","beer"}
print(groceries)

if "milk" in groceries:
    print("You already have milk hoss!")
else:
    print("Oh yes, you need milk!")


#dictionaries
#keys before colon, values after colon
classmates = {"Tony":"cool but smells", "Emma":"sits behind me","Lucy":"asks too many questions"}
print(classmates)
print(classmates["Emma"])

#k stands for keys, v stands for values
for k,v in classmates.items():
    print(k+v)


#modules
def fish():
    print("I am a tuna feesh")