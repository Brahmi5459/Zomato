#Zomato Registration
print("Zomato Registration")
nme=input("enter your name:")
phno=input("enter your phone number:")
pwd=input("enter your password:")
gender=input("Enter your gender:")
#Zomato login
print("Zomato Login")
phone_number=" "
password=" "
name=" "
name=input("Enter your name")
phone_number=input("please enter your phone number:")
password=input("Please enter your password:")

while phone_number!=phno or password!=pwd or name!=nme:
    if name!=nme:
        print("You entered the wrong name")
        name=input("Please enter your name again!")
    elif phone_number!=phno:
        print("You entered the wrong phone number")
        phone_number=input("please enter your phone number again!") 
    elif password!=pwd:
        print("You entered the wrong password")
        password=input("Please enter your password again!")
print("welcome to zomato")
#booking fooditem


fooditems=["gongura chutney","perugu chutney","chicken biryani","chicken dum biryani","prawns biryani","starters","mutton biryani","mutton dum biryani"]

amount=" "
delivery_to_our_home=" "
while(True):
    customer=input("search your fooditem")
    if customer.strip() in fooditems:
        print("your fooditem is available")
        print("pay amount to zomato on online")
        amount=input("please enter amount")
        print("food item is deliverd to our home")
        delivery_to_our_home=input("we can start for eating food")
    elif customer.strip()==amount:
        print("you can pay amount for that food")
    elif customer.strip()==delivery_to_our_home:
        print("we can start for eating the food")
    else:
        print("your food item is not available")
    

'''output:-
----------
enter your phone number:9502538316
enter your otp:4321
enter your name:brahmi
enter your phone number9502538316
enter your otp4321
enter your namebrahmi
welcome to zomato
search your fooditembiryani
your fooditem is available
pay amount to zomato on online500
we can start for eating food
=== RESTART: C:/Users/Brahmi/AppData/Local/Programs/Python/Python39/zomato.py ==
search your fooditembiryani             
your fooditem is available
pay amount to zomato on online500
we can start for eating food'''

