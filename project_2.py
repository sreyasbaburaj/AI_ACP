import random
def calc(x, y):
    operator = input(
        "What operation would you like to perform? Like add, subtract, multiply, divide. "
    )
    if operator.lower() == "add":
        print("The result is ", x + y)
    elif operator.lower() == "subtract":
        print("The result is ", x - y)
    elif operator.lower() == "multiply":
        print("The result is ", x * y)
    elif operator.lower() == "divide":
        print("The result is ", x / y)
    else:
        print("Invalid operator. Try again.")

def joke():
    list=[["Why don't scientists trust atoms?", "Because they make up everything!"],
          ["Why did the scarecrow win an award?", "Because he was outstanding in his   field!"],
          ["Why don't skeletons fight each other?", "They don't have the guts."],
          ["What do you call fake spaghetti?", "An impasta!"],
          ["Why did the bicycle fall over?", "Because it was two-tired!"]]
    if len(list)==0:
        print("Sorry, no more jokes for today! Come back another day!")
    while len(list)>0:
        r=random.randint(0,4)
        jk=input(list[r][0])
        print(list[r][1])
        ask=input("Do you want to hear another joke?").lower()
        if "yes" in ask:
            list[r].pop()
        elif "no" in ask:
            break

print("Hello.")
a = input("What is your name? ")
print(f"Well nice to meet you {a} ")

while True:
    b = input("How are you feeling today? ")
    if b.lower() == "great" or b.lower() == "good":
        print("Good to hear you are doing well.")
        print("What feature of our chatbot do you want to explore?")
        c = input("We have a simple calculator and a joke generator. ").lower()
        if "calculator" in c:
            print("Let's do some math!")
            d = int(input("Enter a number: "))
            e = int(input("Enter another number: "))
            calc(d, e)
        elif "joke" in c:
            joke()
    elif b.lower() == "bad" or b.lower() == "not good":
        print("I am sorry to hear that. Hope things get well soon.")
    else:
        print("I get it. Sometimes it's hard to describe what we feel.")

    exit = input("Would you like to exit or continue(Yes or No): ")
    if exit.lower() == "yes":
        print("Goodbye!")
        break
    else:
        print("Ok, lets keep going.")