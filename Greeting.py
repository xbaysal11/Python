def greetingPerson():

  print('Welcome to Vacation Planner!')

  name = raw_input ("What is your name: ")
  print("Nice to meet you",name,",where are you traveling to?")

  place = raw_input()
  print("Great!",place,"sounds like a great trip")

greetingPerson()
print("***********\n")

def travelTimeBudget():

  day = int(raw_input("How many days are you going to spend traveling?"))
  money = float(raw_input("How much money, in USD, are you planning to spend on your trip:"))
  currency = str(raw_input("What is the three letter currency symbol for your travel destination?"))
  conversion = float(raw_input("How many %s are there in 1 USD?"%currency))
  
  hour = day * 24
  minute = hour * 60
  second = minute * 60
  perday = money / day
  eur = money * conversion
  perdayeur = eur / day
 

  print("If you are traveling for",day," days that is same as ",hour," hours or ",minute," minuts or ",second," seconds.")
  print("If you are going to spend $",money,"USD that means per day you can spend up to $",round(perday,1),"USD")
  print("Your total budget in ",currency," is ",eur,currency,", which per day is ",round(perdayeur,2),currency)

  
  
travelTimeBudget()

print("***********\n")

